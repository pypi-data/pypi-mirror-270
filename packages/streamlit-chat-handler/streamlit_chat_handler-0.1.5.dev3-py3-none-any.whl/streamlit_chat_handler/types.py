from pydantic import BaseModel, Field
from typing import Any, Literal, List, Dict

import streamlit as st
from collections import OrderedDict


class StreamlitChatElement(BaseModel):
    """Represents a chat element within a Streamlit application, handling its rendering.

    This model defines a chat element's role (user or assistant), type (e.g., 'text', 'image'), 
    and content along with any additional arguments or keyword arguments used in rendering 
    the content using Streamlit's API.

    Attributes:
        role (Literal["user", "assistant"]): Defines whether the message is from a user or an assistant.
        type (str): Specifies the Streamlit widget type to be used for rendering (e.g., 'text', 'markdown').
        content (Any): The content to be passed to the Streamlit widget, whose type depends on the `type` attribute.
        args (List[Any]): Additional positional arguments for the Streamlit widget.
        kwargs (Dict[str, Any]): Additional keyword arguments for the Streamlit widget.

    Methods:
        render: Render the chat element using the specified Streamlit widget.
    """
    role: Literal["user", "assistant"]
    type: str
    content: Any
    parent: str | None = None
    index: str | None = None
    args: List[Any] = Field(default_factory=list)
    kwargs: Dict[str, Any] = Field(default_factory=dict)
    parent_args: List[Any] | None = None
    parent_kwargs: Dict[str, Any] | None = None

    def render(self):
        """Render the chat element using the specified Streamlit widget.

        This method dynamically calls a Streamlit function based on the `type` attribute, passing
        `content`, `args`, and `kwargs` to it. The rendering context is defined by the `role`, using
        Streamlit's `chat_message` method.

        Returns:
            The result of the Streamlit function call, typically a Streamlit component instance.

        Example:
            # Assuming an instance `chat_element` with type 'text':
            chat_element.render()  # This would render the content using `st.text()`.
        """

        chat_message = st.chat_message(self.role)
        _parent = getattr(chat_message, self.parent)(*self.parent_args, **self.parent_kwargs) if self.parent else chat_message
        return getattr(_parent, self.type)(self.content, *self.args, **self.kwargs)


class UserFeedback(BaseModel):
    positive_button: bool | None = None
    negative_button: bool | None = None
    comment: str | None = None

class StreamlitRenderResponse(BaseModel):
    rendered_elements: OrderedDict[str, Any]
    feedback_metadata: OrderedDict[str, UserFeedback]