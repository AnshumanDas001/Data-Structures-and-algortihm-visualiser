import React from 'react'
import mergeSortImage from '../images/mergeSort.png'
import { useState } from 'react';
import Modal from "./Modal";

const KadaneCard = () => {
  const [open, setOpen] = useState(false);
  return (
    <>
    <div className="h-[375px] w-[360px] bg-white rounded-2xl shadow-md p-4 flex flex-col items-center
                    transition-transform duration-300 ease-in-out hover:scale-105 hover:shadow-xl cursor-pointer"
                    onClick={() => setOpen(true)}>
      
      {/* Image container */}
      <div className="w-full h-[180px] bg-gray-300 rounded-lg mb-4 p-2 flex items-center justify-center">
        <img 
          src={mergeSortImage}
          alt="Merge Sort Illustration" 
          className="max-h-full max-w-full object-contain"
        />
      </div>

      {/* Text Content */}
      <h1 className="text-xl font-semibold text-gray-800 mb-2">Merge Sort</h1>
      <p className="text-sm text-gray-600 text-center px-2">
        Merge Sort is a divide-and-conquer algorithm. It divides the input array 
        into two halves, calls itself for the two halves, and then merges the two 
        sorted halves.
      </p>
    </div>
    {open && (
        <Modal onClose={() => setOpen(false)}>
          <h2 className="text-2xl font-bold mb-4">Merge Sort Details</h2>
          <p>Here's where you can show a full explanation or visualization of Merge Sort.</p>
        </Modal>
      )}
    </>
  )
}

export default KadaneCard
