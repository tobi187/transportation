open System

let input_field = [
    "  ####   "
    "###  ####"
    "#     $ #"
    "# #  #$ #"
    "# . .#P #"
    "#########"
]

let moves = ["r"; "u"; "u"; "l"; "l"; "l"; "u"; "l"; "d"; "r"; "r"; "r"; "r"; "d"; "d"; "l"; "u"; "r"; "u"; "l"; "l"; "l"; "d"; "d"; "l"; "l"; "l"; "u"; "u"; "r"; "r"; "d"; "r"; "d"; "l"; "u"; "u"; "u"; "r"; "d"; "d"]

let player_symbol = "P"
let goal_symbol = "."
let stone_symbol = "$"
let wall_symbol = "#"
let free_symbol = " "


(*let find_postions (index:int) (line:string) =
    match line.Contains player_symbol with
    | true -> player_pos <- (index, line.IndexOf player_symbol)
    | false -> ()

    match line.Contains goal_symbol with
    | true ->
        Seq.iteri (fun i x -> match x.ToString() = goal_symbol with
                              | true -> goals <- Array.append goals [|(index, i)|]
                              | false -> () ) line
    | false -> ()*)

let calcPositions index =
    let cols = input_field.[0].Length
    let rowNr = index / cols
    let rest = index % cols
    (Convert.ToInt32 rowNr, rest)

let findPostions i x =
    match x.ToString() with
    | "." -> i
    | _ -> -1


let goals = 
    input_field
    |> List.reduce (+)
    |> Seq.mapi findPostions
    |> Seq.filter (fun x -> x <> -1)
    |> Seq.map calcPositions
    |> Seq.toArray


let player_pos = 
    input_field
    |> List.reduce (+)
    |> Seq.findIndex (fun x -> x.ToString() = player_symbol)
    |> calcPositions


let field: char[,] = Array2D.init input_field.Length input_field.[0].Length (fun i1 i2 -> (input_field.[i1]).[i2])

//let mutable is_cheating = false

let make_move (curr_pos: int*int) move =
    match move with
    | x when x = "l" || x = "L" ->
        let r, c = curr_pos
        (r, c - 1)
    | x when x = "r" || x = "R" ->
        let r, c = curr_pos
        (r, c + 1)
    | x when x = "u" || x = "U" ->
        let r, c = curr_pos
        (r - 1, c)
    | x when x = "d" || x = "D" ->
        let r, c = curr_pos
        (r + 1, c)
    | _ -> (-1, -1)

let eval_move (curr_field: string[,]) curr_move (pos: int*int) =
    let row, col = pos
    let curr_pos = Array2D.get curr_field row col

    match curr_pos.ToString() with
    | a when a = wall_symbol -> (-1, -1)
    | a when a = free_symbol || a = goal_symbol -> pos
    | a when a = stone_symbol ->
        let row2, col2 = make_move pos curr_move
        match (Array2D.get curr_field row2 col2).ToString() with
        | a when a = goal_symbol || a = free_symbol -> (row2, col2)
        | _ -> (-1, -1)
    | _ -> (-1, -1)


let set_goals goal_pos curr_field =
    let row, col = goal_pos
    match (Array2D.get curr_field row col).ToString() with
    | a when a = stone_symbol || a = player_symbol || a = goal_symbol -> ()
    | _ -> Array2D.set curr_field row col goal_symbol

let operation curr_field curr_pos curr_move =
    //printfn "%A" curr_field
    

    let new_pos = make_move curr_pos curr_move
    match new_pos with
    | (a, b) when a < 0 || b < 0 -> failwith "is Cheating" //is_cheating <- true
    | _ -> ()

    let stone_or_next_pos = eval_move curr_field curr_move new_pos
    match stone_or_next_pos with
    | (a, b) when a < 0 || b < 0 -> failwith "is Cheating" // is_cheating <- true
    | _ -> ()

    let old_player_pos_row, old_player_pos_col = curr_pos
    let new_player_pos_row, new_player_pos_col = new_pos
    Array2D.set curr_field new_player_pos_row new_player_pos_col player_symbol
    Array2D.set curr_field old_player_pos_row old_player_pos_col free_symbol

    match new_pos = stone_or_next_pos with
    | true -> ()
    | false ->
        let stone_row, stone_col = stone_or_next_pos
        Array2D.set curr_field stone_row stone_col stone_symbol


    (curr_field, new_pos)


let check_is_finished goal_pos my_field =
    let row, col = goal_pos
    match (Array2D.get my_field row col).ToString() = stone_symbol with
    | true -> ()
    | false -> failwith "is Cheating" // is_cheating <- true


let rec play game_field pos move_list =
    match move_list with
    | [] -> 
        Array.iter (fun x -> check_is_finished x game_field) goals
        false
    | head :: tail ->
        let new_game_field, new_player_pos = operation game_field pos head
        //if is_cheating then failwith "You cheated"
        Array.iter (fun x -> set_goals x game_field) goals
        play new_game_field new_player_pos tail


// let workflow() =

//     let mutable game_field = field |> Array2D.map string

//     for move in moves do
//         printfn "%A" game_field
//         printfn "%s" "______________________________________________" 
//         let m, n = operation game_field player_pos move
//         if is_cheating then failwith "You cheated"
//         game_field <- m
//         //game_field <- Array.iter (f)
//         Array.iter (fun x -> set_goals x game_field) goals
//         player_pos <- n


//     Array.iter (fun x -> check_is_finished x game_field) goals

//     is_cheating


// printfn "hei there: %A" (workflow())

play (field |> Array2D.map string) player_pos moves |> printfn "cheating: %b"