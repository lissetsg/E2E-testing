import os
from playwright.sync_api import sync_playwright
import shutil

def before_all(context):
    context.playwright = None
    context.browser = None
    chrome_path = "/opt/google/chrome/chrome"
    if not os.path.exists(chrome_path):
        chrome_path = shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser")
    context.playwright = sync_playwright().start()
    launch_args = {"headless": False}
    if chrome_path and os.path.exists(chrome_path):
        launch_args["executable_path"] = chrome_path
    context.browser = context.playwright.chromium.launch(**launch_args)
    context.context = context.browser.new_context()
    context.page = context.context.new_page()

def after_all(context):
    if hasattr(context, 'page'):
        context.page.close()
    if hasattr(context, 'context'):
        context.context.close()
    if hasattr(context, 'browser'):
        context.browser.close()
    if hasattr(context, 'playwright'):
        context.playwright.stop()
