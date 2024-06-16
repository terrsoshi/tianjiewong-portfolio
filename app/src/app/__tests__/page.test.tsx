import { render, screen } from "@testing-library/react";

import Home, { fetchData } from "../page";

describe("Home", () => {
  // Before each test in this test suite
  beforeEach(async () => {
    // Render the Home page
    render(await Home());
  });

  // Simple Test for rendering the Home page correctly
  test("should render a paragraph", () => {
    const paragraph = screen.getByText("Get started", { exact: false });
    expect(paragraph).toBeInTheDocument();
  });
});

describe("fetchData()", () => {
  // Test for successful data fetching
  test("should fetch data", async () => {
    const expected = "Hello World!";
    // Mock successful response from fetch
    global.fetch = jest.fn(() =>
      Promise.resolve({
        json: () => Promise.resolve(expected),
      }),
    ) as jest.Mock;
    await expect(fetchData()).resolves.toBe(expected);
    expect(global.fetch).toHaveBeenCalled();
  });

  // Test for handling error while fetching data
  test("should handle error", async () => {
    const expected = new Error("Failed to fetch data.");
    // Mock failing responses from fetch
    global.fetch = jest.fn(() =>
      Promise.resolve({
        json: () => Promise.reject(expected),
      }),
    ) as jest.Mock;
    await expect(fetchData()).rejects.toBe(expected);
    expect(global.fetch).toHaveBeenCalled();
  });
});
