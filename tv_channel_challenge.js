export function getSortedShows(shows, times) {
    //Implement this for the first scenario
    const output = []
    const programm = {
        title: null
        starttime: null
        url: null
    }
    shows.forEach(function(show)){
        let html_wrap = document.createElement("p")
        const title_with_css = show.title.classList.add("title")
        html_wrap.appendChild(title_with_css)

        if ()
    }
    
    throw new Error("Not implemented");
}

export function getProgress(width, duration, current) {
    //Implement this for the second scenario
    throw new Error("Not implemented");
}
