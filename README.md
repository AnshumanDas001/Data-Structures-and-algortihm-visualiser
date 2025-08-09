# Sorting Visualizer

A web application to visualize and understand popular sorting algorithms and related data structure algorithms. Built with React and Vite, this project provides interactive, animated visualizations to help users learn how sorting algorithms work step by step.

## Features

- Visualize multiple sorting algorithms (e.g., Bubble Sort, Merge Sort, etc.)
- Step-by-step animation of sorting processes
- Adjustable array size and speed controls
- Interactive UI for selecting algorithms
- Additional algorithm visualizations (e.g., Kadane's, Dijkstra's)
- Exportable reports and plots (Python integration)


## Getting Started

### Prerequisites
- Node.js (v14 or higher recommended)
- npm or yarn

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AnshumanDas001/Data-Structures-and-algortihm-visualiser.git
   cd Data-Structures-and-algortihm-visualiser
   ```
2. **Install dependencies:**
   ```bash
   npm install
   # or
   yarn install
   ```
3. **Start the development server:**
   ```bash
   npm run dev
   # or
   yarn dev
   ```
4. **Open your browser:**
   Visit `http://localhost:5173` (or the port shown in your terminal)

## Project Structure

- `src/Algorithms/` — Sorting algorithm implementations
- `src/Components/` — React components for UI and algorithm cards
- `src/assets/` — Static assets (images, icons)
- `src/images/` — Algorithm illustration images
- `src/Components/iv_skew_plot.py` — Python script for generating PDF plots/reports

## Technologies Used

- [React](https://react.dev/)
- [Vite](https://vitejs.dev/)
- [ReportLab](https://www.reportlab.com/) (Python, for PDF generation)
- [matplotlib](https://matplotlib.org/) (Python, for plotting)
- [nptdms](https://nptdms.readthedocs.io/) (Python, for TDMS file handling)

## Contributing

Contributions are welcome! Please open issues or pull requests for improvements, bug fixes, or new features.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
