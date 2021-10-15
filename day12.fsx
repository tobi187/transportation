open System

let readfile = IO.File.ReadAllLines """P:\projects\learning\f#\start\advent_of_code_challenges\advent_of_code_challenges\moves12.txt"""

let mutable register = Map.empty.Add("a", 0).Add("b", 0).Add("c", 0).Add("d", 0)

let mutable jump_index = 0

let digits = [1..9]

let copy (inp:string[]) = 
    match Int32.TryParse (inp.[1].ToString()) with
    | true, _ -> 
        Map.add inp.[2] (int inp.[1])  register
    | false, _ ->
        let val_of_x = Map.find inp.[1] register
        Map.add inp.[2] val_of_x register


let inc (inp:string[]) =
    let old_val = Map.find inp.[1] register
    Map.add inp.[1] (old_val + 1) register

let dec (inp:string[]) =
    let old_val = Map.find inp.[1] register
    Map.add inp.[1] (old_val - 1) register

let jnz (inp:string[]) = 
    match Int32.TryParse (inp.[1].ToString()) with
    | true, a ->
        printfn "im a %i" a
        if a <> 0 then jump_index <- a
        register
    | false, _ ->
        if (Map.find inp.[1] register) <> 0 then jump_index <- (int inp.[2]) 
        register

let check_operation (line:String) =
    let splitted_lines = line.Split([|" "|], StringSplitOptions.RemoveEmptyEntries)
    match splitted_lines.[0] with
    | "cpy" -> copy splitted_lines
    | "inc" -> inc splitted_lines
    | "dec" -> dec splitted_lines
    | "jnz" -> jnz splitted_lines
    | _ -> register

let workflow = 
    let mutable line = 0
    while line < (Array.length readfile - 1) do
        register <- check_operation readfile.[line]
        printfn "%A" register
        if jump_index <> 0 then
            line <- line + jump_index
            jump_index <- 0
        else
            line <- line + 1
    printfn "%i" (Map.find "a" register)
