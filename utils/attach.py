import allure


def attach_text(name: str, content: str):
    allure.attach(
        content,
        name=name,
        attachment_type=allure.attachment_type.TEXT,
        extension=".txt",
    )
