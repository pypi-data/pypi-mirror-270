"""
Copyright 2021-2024 Vitaliy Zarubin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from alive_progress import alive_bar

from backupz.src.support.output import echo_stdout


class ProgressAliveBar:
    def __init__(self, message_success=None) -> None:
        super().__init__()
        self.transferred_up = 0
        self.alive_bar_instance = None
        self.message_success = message_success

    def update(
            self,
            transferred: int,
            total: int,
    ) -> None:
        if not self.alive_bar_instance:
            self._dispatch_bar()
        self.bar(transferred / total)
        if transferred >= total:
            self._destroy_bar()
            if self.message_success:
                echo_stdout(self.message_success)

    def up(
            self,
            transferred: int,
            total: int,
    ) -> None:
        self.transferred_up += transferred
        if self.transferred_up > total - transferred:
            self.update(total, total)
        else:
            self.update(self.transferred_up, total)

    def spinner_start(self, title: str | None = "") -> None:
        if not self.alive_bar_instance:
            self._dispatch_bar_spinner(title)

    def spinner_end(self) -> None:
        self._destroy_bar()
        if self.message_success:
            echo_stdout(self.message_success)

    def _dispatch_bar_spinner(self, title: str | None = "") -> None:
        self.alive_bar_instance = alive_bar(monitor=None, stats=None, title=title, stats_end=False)
        self.bar = self.alive_bar_instance.__enter__()

    def _dispatch_bar(self, title: str | None = "") -> None:
        self.counter = 0
        self.transferred_up = 0
        self.alive_bar_instance = alive_bar(manual=True, title=title, stats='({eta})', stats_end=False)
        self.bar = self.alive_bar_instance.__enter__()

    def _destroy_bar(self) -> None:
        self.alive_bar_instance.__exit__(None, None, None)
