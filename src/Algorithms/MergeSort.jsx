import React, { useState, useEffect } from "react";

const MergeSortVisualizer = () => {
  const initialArray = [13, 18, 5, 17, 11, 9, 6, 16, 14, 400, 3, 2, 8, 7, 19, 1, 20, 10, 12, 4];
  const [array, setArray] = useState(initialArray);
  const [steps, setSteps] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);
  const [isPaused, setIsPaused] = useState(false);

const handlePauseResume = () => {
  setIsPaused(prev => !prev);
};

const handleRestart = () => {
  setCurrentStep(0);
  setArray(initialArray);
  setIsPaused(false);
};


  useEffect(() => {
    const arr = [...initialArray];
    const snapshots = [];

    const merge = (arr, l, m, r) => {
      const left = arr.slice(l, m + 1);
      const right = arr.slice(m + 1, r + 1);
      let i = 0, j = 0, k = l;

      while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) arr[k++] = left[i++];
        else arr[k++] = right[j++];
        snapshots.push([...arr]);
      }

      while (i < left.length) {
        arr[k++] = left[i++];
        snapshots.push([...arr]);
      }

      while (j < right.length) {
        arr[k++] = right[j++];
        snapshots.push([...arr]);
      }
    };

    const mergeSort = (arr, l, r) => {
      if (l >= r) return;
      const m = Math.floor((l + r) / 2);
      mergeSort(arr, l, m);
      mergeSort(arr, m + 1, r);
      merge(arr, l, m, r);
    };

    mergeSort(arr, 0, arr.length - 1);
    setSteps(snapshots);
  }, []);

  useEffect(() => {
    if (steps.length > 0 && currentStep < steps.length && !isPaused) {
      const timer = setTimeout(() => {
        setArray(steps[currentStep]);
        setCurrentStep(currentStep + 1);
      }, 250);
  
      return () => clearTimeout(timer);
    }
  }, [steps, currentStep, isPaused]);
  

  return (
<>
<div className="flex justify-center mt-4 gap-4">
    <button
        onClick={handlePauseResume}
        className="bg-yellow-400 text-black px-4 py-2 rounded-lg font-semibold hover:bg-yellow-500 transition"
    >
        {isPaused ? "Resume" : "Pause"}
    </button>
    <button
        onClick={handleRestart}
        className="bg-red-500 text-white px-4 py-2 rounded-lg font-semibold hover:bg-red-600 transition"
    >
        Restart
    </button>
    </div>
    <div className="flex justify-center items-end gap-4 h-[400px] mt-8">


        
      {array.map((val, idx) => (
        <div
          key={idx}
          className="bg-purple-500 rounded-lg shadow-md"
          style={{
            height: `${val * 30}px`, 
            width: "40px",           
            transition: "all 0.3s ease-in-out",
          }}
        />
      ))}
    </div>
</>
  );
};

export default MergeSortVisualizer;
