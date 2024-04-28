# SPDX-FileCopyrightText: 2024-present OLIST TINY TECNOLOGIA LTDA
#
# SPDX-License-Identifier: MIT
from http import HTTPStatus

from django.http import HttpRequest, HttpResponse
from django.views import View


class PingView(View):
    http_method_names = [
        "get",
        "head",
        "options",
        "trace",
    ]

    async def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("Pong", status=HTTPStatus.OK)
