let check_one l = 
  let rec check_one' acc_double acc_incr = function
    | [] | _ :: [] -> (acc_double && acc_incr)
    | x :: y :: xs -> check_one' ((x = y) || acc_double) ((x <= y) && acc_incr) (y :: xs)
  in
  check_one' false true l

let check_two l =
  let rec check_two' acc_incr acc_double same = function
    | [] | _ :: [] -> (acc_incr && ((same = 1) || acc_double))
    | x :: y :: xs when (x = y) -> check_two' acc_incr acc_double (same + 1) (y :: xs)
    | x :: y :: xs -> check_two' ((x <= y) && acc_incr) ((same = 1) || acc_double) 0 (y :: xs)
  in
  check_two' true false 0 l

let digits x =
  let rec digits' acc = function
    | a when a < 10 -> a ::acc
    | a -> digits' ((a mod 10) :: acc) (a/10)
  in 
  digits' [] x

(* to check: 125730-579381 *)

let checking = 
  let lower = 125730 in
  let upper = 579381 in
  let rec checking' found_one found_two = function
    | a when a >= upper -> (found_one, found_two)
    | a when check_two (digits a) -> checking' (found_one + 1) (found_two + 1) (a+1)
    | a when check_one (digits a) -> checking' (found_one + 1) (found_two) (a+1)
    | a -> checking' found_one found_two (a+1)
  in
  checking' 0 0 lower
