function SearchBar({search,setSearch}){
    return(
        <>
        <input placeholder="SEARCH..." value={search} onChange={(e)=>setSearch(e.target.value)} />
        </>
    );
}
export default SearchBar;