from __future__ import annotations

from typing import Union

from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.validation import Integer
from textual.widget import Widget
from textual.widgets import Button, Checkbox, Input


class RunQueryBar(Horizontal):
    def __init__(
        self,
        *children: Widget,
        name: Union[str, None] = None,
        id: Union[str, None] = None,  # noqa
        classes: Union[str, None] = None,
        disabled: bool = False,
        max_results: int = 10_000,
    ) -> None:
        self.max_results = max_results
        super().__init__(
            *children, name=name, id=id, classes=classes, disabled=disabled
        )

    def compose(self) -> ComposeResult:
        yield Checkbox("Limit ", id="limit_checkbox")
        yield Input(
            str(min(500, self.max_results)),
            id="limit_input",
            validators=Integer(
                minimum=0,
                maximum=self.max_results if self.max_results > 0 else None,
                failure_description=(
                    f"Please enter a number between 0 and {self.max_results}."
                    if self.max_results > 0
                    else "Please enter a number greater than 0."
                ),
            ),
        )
        yield Button("Run Query", id="run_query")

    def on_mount(self) -> None:
        self.checkbox = self.query_one(Checkbox)
        self.input = self.query_one(Input)
        self.button = self.query_one(Button)
        if self.app.is_headless:
            self.input.cursor_blink = False

    def on_input_changed(self, message: Input.Changed) -> None:
        """
        check and uncheck the box for valid/invalid input
        """
        if message.input.id == "limit_input":
            if (
                message.input.value
                and message.validation_result
                and message.validation_result.is_valid
            ):
                self.checkbox.value = True
            else:
                self.checkbox.value = False

    @property
    def limit_value(self) -> int | None:
        if not self.checkbox.value or not self.input.is_valid:
            return None
        try:
            return int(self.input.value)
        except ValueError:
            return None

    def set_not_responsive(self) -> None:
        self.add_class("non-responsive")

    def set_responsive(self) -> None:
        self.remove_class("non-responsive")
