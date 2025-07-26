import BubbleCard from './Components/BubbleCard'
import DijkCard from './Components/DijkCard'
import KadaneCard from './Components/KadaneCard'
import MergeCard from './Components/MergeCard'

import './index.css' 
function App() {

  return (
<>
  {/* Gradient Background Full Screen */}
  <div className="min-h-screen w-full bg-gradient-to-br from-indigo-900 via-purple-900 to-black flex flex-col items-center">
    
    {/* Title */}
    <div className="w-full text-center pt-8 pb-4 mb-30">
      <h1 className="text-4xl font-bold bg-gradient-to-r from-cyan-400 via-purple-400 to-pink-400 text-transparent bg-clip-text">
        DATA STRUCTURES AND ALGORITHM VISUALIZER
      </h1>
    </div>

    {/* Card Section */}
    <div className="flex flex-wrap justify-center gap-8 mt-6">
      <BubbleCard />
      <DijkCard />
      <KadaneCard />
      <MergeCard />
    </div>
    
  </div>
</>



  )
}

export default App
