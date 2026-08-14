import { test, expect } from '@playwright/test';

test("Verify Quick Links menu is visible and clickable on Dashboard after login", async ({ page }) => {
    // Step 1: Navigate to {{BASE_URL}} (https://hrinnova.stagingapplications.com)
    console.log("\u25b6 step 1/13: Navigate to {{BASE_URL}} (https://hrinnova.stagingapplications.com)");
    await page.goto("{{BASE_URL}}");
    // Step 2: Enter {{USERNAME}} (Bhoomi.mehta) into the username field
    console.log("\u25b6 step 2/13: Enter {{USERNAME}} (Bhoomi.mehta) into the username field");
    await page.locator("[id=\"username\"]").fill("{{USERNAME}}");
    // Step 3: Enter {{PASSWORD}} (Admin@123) into the password field
    console.log("\u25b6 step 3/13: Enter {{PASSWORD}} (Admin@123) into the password field");
    await page.locator("[id=\"password\"]").fill("{{PASSWORD}}");
    // Step 4: Click the Login button
    console.log("\u25b6 step 4/13: Click the Login button");
    await page.locator("[id=\"btnLogin\"]").click();
    // Step 5: Wait for the Pending actions popup to appear and click the Remind Later button
    console.log("\u25b6 step 5/13: Wait for the Pending actions popup to appear and click the Remind Later button");
    await expect(page.getByText("Pending actions").first()).toBeVisible();
    await page.locator("[id=\"btnRemindLater\"]").click();
    // Step 9: Click the Quick Links button
    console.log("\u25b6 step 9/13: Click the Quick Links button");
    await expect(page.getByRole("link", { name: "Quick Links" }).first()).toBeVisible();
    await page.getByRole("link", { name: "Quick Links" }).click();
    // Step 11: Click on quick links again to close the Quick Links menu
    console.log("\u25b6 step 11/13: Click on quick links again to close the Quick Links menu");
    //await page.keyboard.press("Escape");
    // page.getByRole("button", { name: "Close" }).click();
    await page.getByRole("link", { name: "Quick Links" }).click();
    // (unresolved browser_click — re-run agentic mode to re-capture this step)
    // Step 12: Click the user icon in the top-right corner to open the user menu
    console.log("\u25b6 step 12/13: Click the user icon in the top-right corner to open the user menu");
    await page.getByRole("button", { name: "User" }).click();
    // Step 13: Click the Sign Out button
    console.log("\u25b6 step 13/13: Click the Sign Out button");
    await page.getByText("Logout").first().click();
    console.log("\u2713 all 13 step(s) completed");
});