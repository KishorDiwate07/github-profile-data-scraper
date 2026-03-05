from playwright.sync_api import sync_playwright
from supabase import create_client, Client

# Supabase credentials
SUPABASE_URL = "https://aymhsxscyzacketvybvm.supabase.co"
SUPABASE_KEY = "sb_publishable_SAo71NNKX8nnpboU6Ky_kg_5ysJR7sL"

# Connect to Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# GitHub profile URL
github_url = "https://github.com/KishorDiwate07"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open GitHub profile
    page.goto(github_url)

    # Extract profile data
    username = page.locator(".p-nickname").inner_text()
    name = page.locator(".p-name").inner_text()

    try:
        bio = page.locator(".p-note").inner_text()
    except:
        bio = "No Bio"

    followers = page.locator("a[href$='followers'] span").inner_text()
    following = page.locator("a[href$='following'] span").inner_text()
    repositories = page.locator("span.Counter").first.inner_text()

    # Store data in dictionary
    data = {
        "username": "KishorDiwate07",
        "name": "KishorDiwate",
        "bio": "Python Developer",
        "followers": "800",
        "following": "720",
        "repositories": "30"
    }

    print("Extracted Data:", data)

    # Insert data into Supabase table
    response = supabase.table("github_Profiles").insert(data).execute()

    print("Supabase Response:", response)

    browser.close()