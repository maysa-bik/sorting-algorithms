# Sorting Visualizer 🔄

## Introduction 📚

Sorting Visualizer is a Python application designed to visualize various sorting algorithms through a graphical user
interface (GUI). It allows users to interactively select and visualize how different sorting algorithms manipulate data.

## Table of Contents 📑

- [Introduction 📚](#introduction-)
- [Features 🌟](#features-)
- [Installation 🔧](#installation-)
- [Usage 🚀](#usage-)
- [Supported Sorting Algorithms 📊](#supported-sorting-algorithms-)
- [Dependencies 📌](#dependencies-)
- [Testing 🧪](#testing-)
- [Contributors 👥](#contributors-)
- [License 📄](#license-)

## Features 🌟

- Interactive GUI built with Tkinter.
- Visualization of sorting processes in real-time.
- Support for multiple sorting algorithms including Selection Sort, Bubble Sort, Insertion Sort, Merge Sort, Quick Sort,
  Heap Sort, and Comb Sort.
- Performance measurement for sorting operations.

## Installation 🔧

To run Sorting Visualizer, ensure you have Python and pip installed on your system. You can install all the required
dependencies with the following command:

```
pip install -r requirements.txt
```

## Usage 🚀

To start the application, run the following command in the terminal:

```
python main.py
```

The GUI will open where you can generate data, choose a sorting algorithm, and visualize the sorting process.

## Supported Sorting Algorithms 📊

- **Selection Sort** 🔄: This algorithm sorts an array by repeatedly finding the minimum element from the unsorted part
  and putting it at the beginning. The algorithm maintains two subarrays in a given array.
  Example:
  ```
  Initial array: [64, 25, 12, 22, 11]
  After first iteration: [11, 25, 12, 22, 64]
  After second iteration: [11, 12, 25, 22, 64]
  After third iteration: [11, 12, 22, 25, 64]
  Sorted array: [11, 12, 22, 25, 64]
  ```

- **Bubble Sort** 🛁: This simple sorting algorithm works by repeatedly stepping through the list, comparing each pair of
  adjacent items and swapping them if they are in the wrong order. The pass through the list is repeated until the list
  is sorted.
  Example:
  ```
  Initial array: [5, 3, 8, 4, 2]
  After first iteration: [3, 5, 4, 2, 8]
  After second iteration: [3, 4, 2, 5, 8]
  After third iteration: [3, 2, 4, 5, 8]
  After fourth iteration: [2, 3, 4, 5, 8]
  Sorted array: [2, 3, 4, 5, 8]
  ```

- **Insertion Sort** ➡️: This algorithm builds the final sorted array one item at a time. It is much less efficient on
  large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
  Example:
  ```
  Initial array: [4, 3, 2, 10, 12, 1, 5, 6]
  After first iteration: [3, 4, 2, 10, 12, 1, 5, 6]
  After second iteration: [2, 3, 4, 10, 12, 1, 5, 6]
  After third iteration: [2, 3, 4, 10, 12, 1, 5, 6]
  After fourth iteration: [2, 3, 4, 10, 12, 1, 5, 6]
  Sorted array: [1, 2, 3, 4, 5, 6, 10, 12]
  ```

- **Merge Sort** 🧩: This is a divide and conquer algorithm that was invented by John von Neumann in 1945. It works by
  dividing the unsorted list into n sublists, each containing one element (a list of one element is considered sorted),
  and then repeatedly merges sublists to produce new sorted sublists until there is only one sublist remaining.
  Example:
  ```
  Initial array: [38, 27, 43, 3, 9, 82, 10]
  After first iteration: [27, 38, 43, 3, 9, 82, 10]
  After second iteration: [27, 38, 3, 43, 9, 82, 10]
  After third iteration: [3, 27, 38, 43, 9, 82, 10]
  Sorted array: [3, 9, 10, 27, 38, 43, 82]
  ```

- **Quick Sort** ⚡: This is a divide and conquer algorithm. It works by selecting a 'pivot' element from the array and
  partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the
  pivot. The sub-arrays are then recursively sorted.
  Example:
  ```
  Initial array: [10, 7, 8, 9, 1, 5]
  After first iteration: [1, 5, 7, 8, 9, 10]
  Sorted array: [1, 5, 7, 8, 9, 10]
  ```

- **Heap Sort** 🌳: This is a comparison-based sorting algorithm. Heapsort can be thought of as an improved selection
  sort: like selection sort, heapsort divides its input into a sorted and an unsorted region, and it iteratively shrinks
  the unsorted region by extracting the largest element and moving that to the sorted region.
  Example:
  ```
  Initial array: [12, 11, 13, 5, 6, 7]
  After first iteration: [7, 6, 13, 5, 12, 11]
  After second iteration: [6, 5, 7, 13, 12, 11]
  After third iteration: [5, 6, 7, 13, 12, 11]
  Sorted array: [5, 6, 7, 11, 12, 13]
  ```

- **Comb Sort** 🧹: This is a relatively simple sorting algorithm originally designed to improve upon bubble sort. It
  improves on bubble sort by using a gap sequence to remove turtles, or small values near the end of the list.
  Example:
  ```
  Initial array: [8, 4, 7, 6, 2, 3]
  After first iteration: [2, 4, 3, 6, 7, 8]
  After second iteration: [2, 3, 4, 6, 7, 8]
  Sorted array: [2, 3, 4, 6, 7, 8]
  ```

## Dependencies 📌

- matplotlib==3.8.4
- mplcursors==0.5.2
- ttkthemes==3.2.0

## Testing 🧪

The application includes unit tests for verifying the correctness of the implemented sorting algorithms. These tests can
be run with the following command:

```
python -m unittest test.py
```

## Contributors 👥

- Maysa Bik
- Chaima Bekhaouda

## License 📄

This project is licensed under the MIT License.
