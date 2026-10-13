function SortButtons({setSortBy,setSortTitle,sortTitle,sortRating,setSortRating,setShowAvailable,showAvailable}){
    return(
        <>
         <button onClick={()=>{
            setSortBy('title');
            setSortTitle(sortTitle==='A-Z'?'Z-A':'A-Z')
        }}>
            {sortTitle}
        </button>
        <button onClick={()=>{
            setSortBy('rating');
            setSortRating(sortRating==='highest-lowest'?'lowest-highest':'highest-lowest')
        }}>
            {sortRating==='highest-lowest'?'Lowest-Highest':'Highest-Lowest'}
        </button>
        <button onClick={()=>{
            setShowAvailable(!showAvailable)
        }}>
            {showAvailable?'All Books':'Available Books'}
        </button>
        </>
    );
}
export default SortButtons;