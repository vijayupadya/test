import assert from "node:assert/strict";
import test from "node:test";
import { fibonacci } from "./fibonacci";

test("fibonacci returns the first n numbers", () => {
  assert.deepEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]);
});
