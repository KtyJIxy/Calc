# PyKalc

[Place for pic]

## PyKalc is a highly code-customizable simple calculator based on Python and Kivy (hence - the name).

### List of features:
- Two options button with different tasks on simple and long press;
- Its functions are using python symbols and not mathematical (so "**" instead of '^');
- .kv file is very easily customizable, allowing simple functions and instantaneous change of colors ([even by name](https://www.w3.org/TR/SVG11/types.html#ColorKeywords));
- You can build it to be an .exe or even .apk file.

### How to build:

#### Standalone `.EXE` 
1. Download repository (required files - `Kivy_GUI.py`, `Calc.kv`, `functions_main.py`, `PyKalc.spec` and `icon.ico` if you wish.)
2. Get yourself a [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/). Through command line it will be:
   ```shell
    pip install auto-py-to-exe```
3. Launch it:
    ```shell
    auto-py-to-exe```
4. Use a `PyKalc.spec` as a base file.
5. Add `Calc.kv` as an additional file and `icon.ico` as icon.
6. Recommend selecting `--onefile` option.
7. Wait.
8. You will get not an exactly onefile `.EXE`, it has to be in one folder with other required files, especially `Calc.kv`. Size is circa 20 MB plus 10 KB from code files. RAM usage circa 50 MB.
9. If icon wasn't added, use a [Resource Hacker](http://www.angusj.com/resourcehacker/) for adding it.

#### Android `.apk`
1. Fork this repository.
2. Use Build [action](https://docs.github.com/en/actions/learn-github-actions).
3. Wait about 15 minutes.
4. Download an [Artifact](https://docs.github.com/en/actions/managing-workflow-runs/downloading-workflow-artifacts). Size of an `.apk` is circa 15 MB, installed app — 40 MB.
5. Do some debugging to get it properly starting. Frankly, I'd be happy to do it myself, but Android Studio from Google doesn't like AMD Hardware very very much :anguished: