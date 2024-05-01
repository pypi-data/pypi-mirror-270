import pypipr


def main():
    m = pypipr.ivars(pypipr)
    m = m["module"] | m["variable"] | m["class"] | m["function"]
    m = [x for x in m]
    a = pypipr.iargv(1)
    p = "Masukan Nomor Urut atau Nama Fungsi : "
    m = pypipr.choices(daftar=m, contains=a, prompt=p)

    f = getattr(pypipr, m)

    if a == m:
        pypipr.print_colorize(m)
        print(f.__doc__)

    if pypipr.inspect.isclass(f):
        pypipr.print_log("Class tidak dapat dijalankan.")
    elif pypipr.inspect.ismodule(f):
        pypipr.print_log("Module tidak dapat dijalankan.")
    elif pypipr.inspect.isfunction(f):
        s = pypipr.inspect.signature(f)

        if not a:
            print(m, end="")
            pypipr.print_colorize(s)

        k = {}
        for i, v in s.parameters.items():
            print(f"{i} [{v.default}] : ", end="")
            o = input()
            if len(o):
                try:
                    k[i] = eval(o)
                except Exception:
                    pypipr.print_colorize(
                        "Input harus dalam syntax python.",
                        color=pypipr.colorama.Fore.RED,
                    )

        f = f(**k)
    else:
        # variable
        pass

    pypipr.iprint(f)


if __name__ == "__main__":
    main()
