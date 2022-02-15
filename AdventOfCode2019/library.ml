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

(* file with one line to list *)
let file_one_line_to_list f = open_in f |> input_line |> String.split_on_char ','

(* example of a list -> solution function *)
let part_one input_list = 
  let rec part_one' acc = function
    | [] -> acc
    | x :: xs -> part_one' (acc + module_of_mass (int_of_string x)) xs
  in
  part_one' 0 input_list