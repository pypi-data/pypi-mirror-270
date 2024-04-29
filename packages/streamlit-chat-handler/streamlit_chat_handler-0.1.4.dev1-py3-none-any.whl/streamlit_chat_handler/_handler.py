import uuid
from typing import Any, List, Literal, Tuple
from collections import OrderedDict

import streamlit as st
from loguru import logger
from streamlit.runtime.state.session_state_proxy import SessionStateProxy

from streamlit_chat_handler.types import StreamlitChatElement


class StreamlitChatHandler:
    """Handles the state and rendering of chat elements within a Streamlit session.

    This class manages chat elements in a Streamlit application, allowing for creating,
    storing, and rendering user and assistant messages dynamically. It uses a singleton pattern
    to maintain a unique instance per session.

    Attributes:
        session_state (dict): A reference to Streamlit's session state object.
        session_id (str): The unique identifier for the session.
        elements_label (str): The key used to store chat elements in the session state.

    Example:
        >>> import uuid
        >>> from time import sleep
        >>> import streamlit as st
        >>> from streamlit_chat_handler import StreamlitChatHandler
        >>>
        >>> if "session_id" not in st.session_state:
        >>>     st.session_state["session_id"] = str(uuid.uuid4())
        >>>
        >>> chat_handler = StreamlitChatHandler(
        >>>     st.session_state,
        >>>     session_id=st.session_state["session_id"],
        >>> ).render()
        >>>
        >>> if prompt := st.chat_input("What is up?"):
        >>>     chat_handler.append(role="user", type="markdown", content=prompt, render=True)
        >>>
        >>>     with st.spinner("Processing..."):
        >>>         sleep(1)
        >>>         chat_handler.append(role="assistant", type="markdown", content="answer", render=True)

    """

    _instances: dict[str, "StreamlitChatHandler"] = {}
    elements_label: str = "elements"

    def __new__(cls, session_state: SessionStateProxy, session_id: str):
        """Ensure only one instance per session_id."""
        if session_id not in cls._instances:
            instance = super(StreamlitChatHandler, cls).__new__(cls)
            cls._instances[session_id] = instance
            instance.session_state = session_state
            instance.session_id = session_id
            instance._init_session_state()
            instance.step_counter = -1
        return cls._instances[session_id]

    def __init__(self, session_state: SessionStateProxy, session_id: str):
        """Initialize the instance with the session state and ID."""
        self.session_state = session_state
        self.session_id = session_id
        self._init_session_state()
        self.rendered_elements: OrderedDict[str, Any] | None = OrderedDict({})
        self.step_counter += 1

    def append(
        self,
        role: Literal["user", "assistant"] = None,
        type: str = None,
        content: Any = None,
        index: str | None = None,
        render: bool = False,
        parent: str | None = None,
        parent_args: Tuple[Any, ...] = (),
        parent_kwargs: dict[str, Any] = {},
        chat_element: StreamlitChatElement | None = None,
        *args,
        **kwargs,
    ) -> Any | None:
        """Append a new chat element to the session state.

        Args:
            role: The role of the message ('user' or 'assistant').
            type: The type of the message (e.g., 'text', 'image').
            content: The content of the message.
            index: Optional; a unique identifier for the chat element. Automatically generated if not provided.
            render: Optional; if True, the message is rendered immediately.

        Raises:
            ValueError: If an unsupported type is provided.
        """

        index = self._set_index(index)

        if not chat_element:
            chat_element = self._get_chat_element(
                role,
                type,
                content,
                parent,
                parent_args,
                parent_kwargs,
                *args,
                **kwargs,
            )

        self.session_state[self.elements_label][index] = chat_element

        if render:
            return chat_element.render()
        return self

    def append_multiple(
        self, elements: list[StreamlitChatElement], render: bool = False
    ) -> None:
        """Append multiple chat elements to the session state."""

        chat_element = OrderedDict({self._set_index(): element for element in elements})

        for index, element in chat_element.items:
            self.append(
                role=element.role,
                type=element.type,
                content=element.content,
                index=index,
                render=False,  # Aqui, os componentes serão renderizados separadamente
                parent=element.parent,
                parent_args=element.parent_args,
                parent_kwargs=element.parent_kwargs,
            )

        if render:
            response = self._render_elements(chat_element)

            for index, value in response.items():
                if index in self.rendered_elements:
                    del self.rendered_elements[index]
                self.rendered_elements[index] = value

    def increment_step_counter(self) -> None:
        """Finish the current step."""
        self.step_counter += 1

    def render_last(self) -> None:
        """Render the last added chat element."""
        last_key, last_element = _get_last_item(self.session_state[self.elements_label])
        self.rendered_elements[last_key] = last_element.render()

    def render(self) -> "StreamlitChatHandler":
        """Render all chat elements in the session."""
        self.rendered_elements = self._render_elements(
            self.session_state[self.elements_label]
        )
        return self

    def _init_session_state(self) -> None:
        """Initialize the session state for storing chat elements if it doesn't already exist."""
        if self.elements_label not in self.session_state:
            self.session_state[self.elements_label] = OrderedDict({})

    def _set_index(self, index: str | None) -> str:
        """Set the index for the chat element.

        Args:
            index: The index to set.

        Returns:
            The set index.
        """
        if index is None:
            index = uuid.uuid4().hex
            return f"{str(self.step_counter).zfill(6)}{index}"
        return index

    def _get_chat_element(
        self,
        role: Literal["user", "assistant"] = None,
        type: str = None,
        content: Any = None,
        parent: str | None = None,
        parent_args: Tuple[Any, ...] = (),
        parent_kwargs: dict[str, Any] = {},
        *args,
        **kwargs,
    ):
        args_were_passed = all([_check_argument(arg) for arg in (role, type, content)])

        if args_were_passed:
            return StreamlitChatElement(
                role=role,
                type=type,
                content=content,
                parent=parent,
                parent_args=parent_args,
                parent_kwargs=parent_kwargs,
                args=args,
                kwargs=kwargs,
            )
        else:
            raise ValueError("Missing required arguments for StreamlitChatElement.")

    def _render_elements(
        self,
        chat_element: StreamlitChatElement | OrderedDict[str, StreamlitChatElement],
    ) -> OrderedDict[str, Any]:
        """Render chat elements, handling both individual elements and collections.

        Args:
            chat_element: A single StreamlitChatElement or an OrderedDict of them.

        Returns:
            An OrderedDict where keys are the chat element IDs and values are the rendered elements.
        """

        if isinstance(chat_element, StreamlitChatElement):
            chat_element = OrderedDict({self._set_index(): chat_element})

        chat_element_list = [v for v in chat_element.values()]
        element_groups = _group_elements_by_role(chat_element_list)

        response = OrderedDict({})
        count = 0
        for element_list in element_groups:
            role = element_list[0].role
            chat_message = st.chat_message(role)
            for element in element_list:
                try:
                    parent = (
                        getattr(chat_message, element.parent)(
                            *element.parent_args, **element.parent_kwargs
                        )
                        if element.parent
                        else chat_message
                    )
                    response[list(chat_element)[count]] = getattr(parent, element.type)(
                        element.content, *element.args, **element.kwargs
                    )
                except Exception as err:
                    logger.warning(
                        f"Error rendering element {element} in key {list(chat_element)[count]}: {err}"
                    )
                count += 1

        return response


def _get_last_item(ordered_dict: OrderedDict) -> Tuple[str, Any]:
    """Retrieve the last key-value pair from an OrderedDict.

    This function fetches the last key and its corresponding value from an OrderedDict
    without removing them.

    Args:
        ordered_dict (OrderedDict): The dictionary from which to retrieve the last item.

    Returns:
        tuple: A tuple containing the last key and its corresponding value.

    Raises:
        KeyError: If the dictionary is empty.
    """
    last_key = next(reversed(ordered_dict))
    last_value = ordered_dict[last_key]
    return last_key, last_value


def _group_elements_by_role(
    elements: list[StreamlitChatElement],
) -> list[list[StreamlitChatElement]]:
    """Group elements by their role attribute.

    This function takes a list of StreamlitChatElement instances and groups them into
    sublists, where each sublist contains elements of the same role. It ensures that
    elements are grouped consecutively as per the order in the original list.

    Args:
        elements (List[StreamlitChatElement]): A list of chat elements to be grouped.

    Returns:
        List[List[StreamlitChatElement]]: A list of lists, where each sublist contains elements of the same role.
    """
    grouped_elements = []
    if not elements:
        return grouped_elements

    current_group = []
    current_role = elements[0].role

    for element in elements:
        if element.role == current_role:
            current_group.append(element)
        else:
            grouped_elements.append(current_group)
            current_group = [element]
            current_role = element.role

    if current_group:
        grouped_elements.append(current_group)

    return grouped_elements


def _check_argument(argument: Any):
    if argument is not None:
        return True
    return False
