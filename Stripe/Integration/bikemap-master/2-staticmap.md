# staticmap

Visit
https://stripe-bikemap.appspot.com/map.png?center=47.6,-122.3&zoom=9&size=800x500
in your browser
to see staticmap in action.

(`staticmap` is adapted from [github.com/Luzifer/staticmap].)

## Rendering a Map from JSON data

It's tedious to specify complex parameters in a querystring.
We can send a **JSON request body** to `staticmap` instead.

Use [staticmap_example.json] as an example of the data that you will need to
send as an HTTP `POST` request to
`https://stripe-bikemap.appspot.com/map.png`

The [staticmap_example.json] file contains:

* **Parameters**, such as `center`, `width`, `height`, and `zoom`,
  that define a map of Seattle.
* **Markers**
  * a blue, labeled marker for the Chief Sealth Trail
  * a marker (which defaults to red) at Mount Baker station
  * a yellow marker on Jefferson Park
* **Paths**
  * a purple path along Beacon Avenue
  * a red path for part of the Chief Sealth Trail

### POSTing a request with curl

Let's use the [curl] command-line HTTP client to
send a request to `staticmap`.

Using Curl's descriptive option names:

* `--request POST`: send the `POST` HTTP verb.
* `--data-binary "@staticmap_example.json"`:
  read the *contents* of the file `staticmap_example.json`
  and use that data as the request's body.
* `--output example.png`: save the response body
  to the file `example.png`.

```bash
curl --request POST \
     --data-binary "@staticmap_example.json" \
     https://stripe-bikemap.appspot.com/map.png \
     --output example.png
```

Be sure to sure to run `curl` from the directory where `staticmap_example.json` is located
(the root of this repo).

If you're using [PowerShell Core] on Windows (or Mac or Linux):

```powershell
Invoke-WebRequest -uri https://stripe-bikemap.appspot.com/map.png -Method Post -Infile staticmap_example.json -outfile example.png
```

### Opening an Image Manually

You can open `example.png` in a web browser
or some other image previewer.

If you like,
you can use the following invocations
from the *command-line*
to open `example.png`:

* MacOS:
  * `open example.png` will open the image in the default image viewer
  * `open -a Preview example.png` opens the image in Preview
* Windows (cmd.exe):
  * `start example.png`
* Windows (PowerShell):
  * `Invoke-Item example.png`
* Linux:
  * `xdg-open example.png`

[github.com/Luzifer/staticmap]: https://github.com/Luzifer/staticmap
[staticmap_example.json]: ./staticmap_example.json
[curl]: https://curl.haxx.se/
[PowerShell Core]: https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-6





open S_exp

type prim1 = Add1 | Sub1 | IsZero | IsNum | Not

type prim2 = Plus | Minus | Eq | Lt | Div | Mul

type expr =

  | Num of int

  | Var of string

  | True

  | False

  | Prim1 of prim1 * expr

  | Prim2 of prim2 * expr * expr

  | PrimAnd of expr * expr

  | PrimOr of expr * expr

  | If of expr * expr * expr

  | Let of (string * expr) list * expr

  | Case of expr * (int * expr) list

*(***** AST to S_exp *****)*

let rec s_exp_of_expr = function

  | True ->

​      Sym "true"

  | False ->

​      Sym "false"

  | Num n ->

​      Num n

  | Var var ->

​      Sym var

  | Prim1 (Add1, arg) ->

​      Lst [Sym "add1"; s_exp_of_expr arg]

  | Prim1 (Sub1, arg) ->

​      Lst [Sym "sub1"; s_exp_of_expr arg]

  | Prim1 (IsZero, arg) ->

​      Lst [Sym "zero?"; s_exp_of_expr arg]

  | Prim1 (IsNum, arg) ->

​      Lst [Sym "num?"; s_exp_of_expr arg]

  | Prim1 (Not, arg) ->

​      Lst [Sym "not"; s_exp_of_expr arg]

  | Prim2 (Plus, arg1, arg2) ->

​      Lst [Sym "+"; s_exp_of_expr arg1; s_exp_of_expr arg2]

  | Prim2 (Minus, arg1, arg2) ->

​      Lst [Sym "-"; s_exp_of_expr arg1; s_exp_of_expr arg2]

  | Prim2 (Mul, arg1, arg2) ->

​      Lst [Sym "*"; s_exp_of_expr arg1; s_exp_of_expr arg2]

  | Prim2 (Div, arg1, arg2) ->

​      Lst [Sym "/"; s_exp_of_expr arg1; s_exp_of_expr arg2]

  | Prim2 (Lt, arg1, arg2) ->

​      Lst [Sym "<"; s_exp_of_expr arg1; s_exp_of_expr arg2]

  | Prim2 (Eq, arg1, arg2) ->

​      Lst [Sym "="; s_exp_of_expr arg1; s_exp_of_expr arg2]

  | Let (exps, eval_exp) ->

​      let bindings =

​        Lst

​          (List.map

​             (fun (e : string * expr) ->

​               match e with v, expr -> Lst [Sym v; s_exp_of_expr expr] )

​             exps )

​      in

​      Lst [Sym "let"; bindings; s_exp_of_expr eval_exp]

  | If (e1, e2, e3) ->

​      Lst [Sym "if"; s_exp_of_expr e1; s_exp_of_expr e2; s_exp_of_expr e3]

  | PrimAnd (arg1, arg2) ->

​      Lst [Sym "and"; s_exp_of_expr arg1; s_exp_of_expr arg2]

  | PrimOr (arg1, arg2) ->

​      Lst [Sym "or"; s_exp_of_expr arg1; s_exp_of_expr arg2]

  | Case (arg1, arg2) -> 

​    let cases_list = 

​        List.map

​            (fun (num_val, expr_val) -> 

​                Lst [Num num_val; s_exp_of_expr expr_val])

​            arg2 

​        in

​    Lst [Sym "case"; s_exp_of_expr arg1; Lst cases_list]

let string_of_expr s = s |> s_exp_of_expr |> string_of_s_exp
