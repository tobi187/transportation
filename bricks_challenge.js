export function bricksAndWater(bricksArray) {
    //TODO implement this function
    let storage_place = 0
    let height = 0
    for (const brick of bricksArray){
        if (brick > height){
            height = brick
        }
        else if ( bricksArray.indexOf(brick) !== 0 && bricksArray.indexOf(brick) !== -1){
            continue
        }
        else{
            storage_place = storage_place + (height - brick)
        }
    
    }
    return storage_place

    
}
