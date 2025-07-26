import React from "react";

const Modal = ({ onClose, children }) => {
  return (
    <>
      {/* Overlay Blur */}
      <div className="fixed inset-0 bg-opacity-40 backdrop-blur-sm z-40" onClick={onClose} />

      {/* Modal Content */}
      <div className="fixed inset-0 flex items-center justify-center z-50">
        <div className="bg-white w-[75vw] h-[75vh] rounded-xl p-6 relative shadow-2xl">
          {/* Close Button */}
          <button
            onClick={onClose}
            className="absolute top-4 right-4 text-gray-600 hover:text-black text-xl font-bold"
          >
            ✕
          </button>

          {/* Modal Children */}
          {children}
        </div>
      </div>
    </>
  );
};

export default Modal;
