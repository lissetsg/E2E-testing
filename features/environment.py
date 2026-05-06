import os
import shutil
from playwright.sync_api import sync_playwright
import allure

def before_all(context):
    context.playwright = sync_playwright().start()
    
    chrome_path = "/opt/google/chrome/chrome"
    if not os.path.exists(chrome_path):
        chrome_path = shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser")
    
    launch_args = {
        "headless": os.getenv("HEADLESS", "false").lower() == "true",
        "slow_mo": 500  # 🔍 Útil para debug: ralentiza acciones para ver qué pasa
    }
    if chrome_path and os.path.exists(chrome_path):
        launch_args["executable_path"] = chrome_path
        
    context.browser = context.playwright.chromium.launch(**launch_args)

def after_all(context):
    if hasattr(context, 'browser') and context.browser:
        context.browser.close()
    if hasattr(context, 'playwright'):
        context.playwright.stop()

def before_scenario(context, scenario):
    context.context = context.browser.new_context(
        viewport={"width": 1280, "height": 720},
        ignore_https_errors=True  # Demoblaze tiene mixed content
    )
    context.page = context.context.new_page()
    
    # Configurar timeouts más generosos para Demoblaze (sitio lento)
    context.page.set_default_timeout(20000)
    context.page.set_default_navigation_timeout(30000)

def after_scenario(context, scenario):
    if getattr(scenario, 'status', None) == "failed" and hasattr(context, 'page'):
        try:
            allure.attach(
                context.page.screenshot(full_page=True),
                name=f"failure_{scenario.name.replace(' ', '_')}",
                attachment_type=allure.attachment_type.PNG
            )
            # Adjunta también el HTML para debug
            allure.attach(
                context.page.content(),
                name="page_source",
                attachment_type=allure.attachment_type.TEXT
            )
        except Exception as e:
            print(f"⚠️ Error capturando evidencia: {e}")
            
    if hasattr(context, 'page'):
        context.page.close()
    if hasattr(context, 'context'):
        context.context.close()
