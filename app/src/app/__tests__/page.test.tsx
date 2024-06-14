import { render, screen } from "@testing-library/react";

import axios from "axios";

import Home, { fetchData } from "../page";

// Mock the axios module
jest.mock("axios");
const mockedAxios = jest.mocked(axios);

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
    // Mock successful response from axios.get
    mockedAxios.get.mockResolvedValue({
      data: expected,
    });
    const res = await fetchData();
    expect(mockedAxios.get).toHaveBeenCalled();
    expect(res).toBe(expected);
  });

  // Test for handling error while fetching data
  test("should handle error", async () => {
    const expected = new Error("Failed to fetch data.");
    // Mock failing responses from axios.get
    mockedAxios.get.mockRejectedValue(expected);
    const res = await fetchData();
    expect(mockedAxios.get).toHaveBeenCalled();
    expect(res).toEqual(expected);
  });
});
