(* reads a file into a list of strings *)
let read_file inputfile = 
let lines = ref [] in
let chan = open_in inputfile in
try
  while true; do
    lines := input_line chan :: !lines
  done; !lines
with End_of_file ->
  close_in chan;
  List.rev !lines ;;

let module_of_mass x = (x / 3) - 2

let fuel_of_mass x =
  let rec fuel_of_mass' acc y = 
    let m = module_of_mass y in
    if m > 0 then fuel_of_mass' (acc + m) m else acc
  in
  fuel_of_mass' 0 x
    

let part_one input_list = 
  let rec part_one' acc = function
    | [] -> acc
    | x :: xs -> part_one' (acc + module_of_mass (int_of_string x)) xs
  in
  part_one' 0 input_list

let part_two input_list = 
  let rec part_one' acc = function
    | [] -> acc
    | x :: xs -> part_one' (acc + fuel_of_mass (int_of_string x)) xs
  in
  part_one' 0 input_list



let sol_one = "AdventOfCode2019/inputs/input01.txt" |> read_file |> part_one
let sol_two = "AdventOfCode2019/inputs/input01.txt" |> read_file |> part_two