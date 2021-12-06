function getSortedShows(shows, times) {
    //Implement this for the first scenario
    const output = []
    const programm = {
        title: null,
        starttime: null,
        url: null
    }
    
    for (let show of shows) {
        //let html_title = Document.createElement("p")
        //html_title.className = "title"
        //html_title.innerText = show["title"]

        let start_time = times.find(x => x.id === 1).starttime
        start_time = Math.floor(start_time) + ":" 
        return Math.floor(start_time/60)
    }
    
    throw new Error("Not implemented");
}

function getProgress(width, duration, current) {
    //Implement this for the second scenario
    throw new Error("Not implemented");
}

time_list = [{ starttime: 1080, id: 1 }, { starttime: 625, id: 2 }]

show_list = [
    {
      id: 1, 
      title: "Once upon node.js", 
      duration: 189, 
      description: "A show about the beginning of Javascript", 
      url:"https://task-static-files.s3.eu-central-1.amazonaws.com/tv-show/4.png"
    }, 
    { 
      id: 2, 
      title: "Code runner", 
      duration: 95, 
      description: "", 
      url: "https://task-static-files.s3.eu-central-1.amazonaws.com/tv-show/3.png" 
    }
  ]

let down = getSortedShows(show_list, time_list)

console.log(down)