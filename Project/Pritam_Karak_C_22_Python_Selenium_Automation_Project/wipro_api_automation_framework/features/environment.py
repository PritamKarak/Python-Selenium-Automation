import logging
import textwrap
from pathlib import Path

import allure
from allure_commons.types import AttachmentType
from PIL import Image, ImageDraw, ImageFont

from framework.api_client import APIClient
from framework.config_reader import get_base_url


PROJECT_ROOT = Path(__file__).resolve().parents[1]

SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"
SCREENSHOT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


def before_all(context):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )

    logging.info(
        "Starting Wipro API Automation Framework"
    )

    context.jsonplaceholder = APIClient(
        get_base_url("jsonplaceholder")
    )

    context.automation = APIClient(
        get_base_url("automation_exercise")
    )

    logging.info(
        "JSONPlaceholder API client initialized: %s",
        get_base_url("jsonplaceholder"),
    )

    logging.info(
        "Automation Exercise API client initialized: %s",
        get_base_url("automation_exercise"),
    )


def before_scenario(context, scenario):
    logging.info(
        "Starting scenario: %s",
        scenario.name,
    )


def attach_api_evidence(context, scenario):
    """
    Attach API request/response information to Allure.
    """

    response_wrapper = getattr(
        context,
        "response",
        None,
    )

    if response_wrapper is None:
        return

    try:
        response = response_wrapper.response
    except Exception:
        return

    

    status_code = getattr(
        response,
        "status_code",
        "N/A",
    )

    try:
        allure.attach(
            str(status_code),
            name="Final HTTP Status",
            attachment_type=AttachmentType.TEXT,
        )
    except Exception:
        pass

    

    response_text = getattr(
        response,
        "text",
        "",
    )

    try:
        allure.attach(
            response_text,
            name="Final API Response",
            attachment_type=AttachmentType.TEXT,
        )
    except Exception:
        pass

    request_url = getattr(
        context,
        "response_url",
        None,
    )

    if request_url:
        try:
            allure.attach(
                str(request_url),
                name="Request URL",
                attachment_type=AttachmentType.TEXT,
            )
        except Exception:
            pass

    request_body = getattr(
        context,
        "request_body",
        None,
    )

    if request_body:
        try:
            allure.attach(
                str(request_body),
                name="Request Body",
                attachment_type=AttachmentType.TEXT,
            )
        except Exception:
            pass

    request_params = getattr(
        context,
        "request_params",
        None,
    )

    if request_params:
        try:
            allure.attach(
                str(request_params),
                name="Query Parameters",
                attachment_type=AttachmentType.TEXT,
            )
        except Exception:
            pass

    create_api_screenshot(
        context,
        scenario,
        status_code,
        response_text,
        request_url,
        request_body,
        request_params,
    )


def create_api_screenshot(
    context,
    scenario,
    status_code,
    response_text,
    request_url,
    request_body,
    request_params,
):
    """
    Creates a PNG image containing API execution evidence
    and attaches it to the Allure report.
    """

    try:

        lines = []

        lines.append(
            "WIPRO API AUTOMATION FRAMEWORK"
        )

        lines.append(
            "=" * 80
        )

        lines.append(
            f"Scenario: {scenario.name}"
        )

        lines.append(
            f"Status: {str(scenario.status).upper()}"
        )

        lines.append(
            f"HTTP Status Code: {status_code}"
        )

        lines.append(
            ""
        )

        lines.append(
            "REQUEST"
        )

        lines.append(
            "-" * 80
        )

        lines.append(
            f"URL: {request_url if request_url else 'N/A'}"
        )

        if request_body:
            lines.append(
                f"Body: {request_body}"
            )

        if request_params:
            lines.append(
                f"Parameters: {request_params}"
            )

        lines.append(
            ""
        )

        lines.append(
            "RESPONSE"
        )

        lines.append(
            "-" * 80
        )

        if response_text:
            lines.extend(
                response_text.splitlines()
            )
        else:
            lines.append(
                "No response body"
            )


        wrapped_lines = []

        for line in lines:

            if len(line) <= 110:

                wrapped_lines.append(
                    line
                )

            else:

                wrapped_lines.extend(
                    textwrap.wrap(
                        line,
                        width=110,
                        break_long_words=False,
                        break_on_hyphens=False,
                    )
                )

        try:

            font = ImageFont.truetype(
                "arial.ttf",
                18,
            )

            title_font = ImageFont.truetype(
                "arialbd.ttf",
                22,
            )

        except Exception:

            font = ImageFont.load_default()
            title_font = font


        line_height = 28

        image_width = 1400

        image_height = max(
            700,
            60 + (
                len(wrapped_lines)
                * line_height
            ),
        )


        image = Image.new(
            "RGB",
            (
                image_width,
                image_height,
            ),
            "white",
        )

        draw = ImageDraw.Draw(
            image
        )


        y = 25

        for index, line in enumerate(
            wrapped_lines
        ):

            if index == 0:

                draw.text(
                    (30, y),
                    line,
                    fill="black",
                    font=title_font,
                )

            else:

                draw.text(
                    (30, y),
                    line,
                    fill="black",
                    font=font,
                )

            y += line_height

        

        screenshot_name = (
            scenario.name
            .replace(" ", "_")
            .replace("/", "_")
            .replace("\\", "_")
            .replace(":", "_")
            .replace("?", "_")
            .replace('"', "")
            .replace("'", "")
        )

        status = str(
            scenario.status
        ).split(".")[-1].upper()

        screenshot_path = (
            SCREENSHOT_DIR
            / f"{screenshot_name}_{status}.png"
        )


        image.save(
            screenshot_path,
            "PNG",
        )

        logging.info(
            "API screenshot created: %s",
            screenshot_path,
        )

        with open(
            screenshot_path,
            "rb",
        ) as image_file:

            allure.attach(
                image_file.read(),
                name=f"API Evidence - {status}",
                attachment_type=AttachmentType.PNG,
            )

    except Exception as exc:

        logging.warning(
            "API screenshot creation failed: %s",
            exc,
        )


def after_scenario(context, scenario):

    logging.info(
        "Finished scenario: %s | status=%s",
        scenario.name,
        scenario.status,
    )

    try:

        attach_api_evidence(
            context,
            scenario,
        )

    except Exception as exc:

        logging.warning(
            "Allure evidence collection failed: %s",
            exc,
        )


def after_all(context):

    logging.info(
        "Execution completed"
    )