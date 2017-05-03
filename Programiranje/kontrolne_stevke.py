# =============================================================================
# Kontrolne števke
# =====================================================================@000924=
# 1. podnaloga
# Sestavite funkcijo `vsota_kvadratov_stevk(n)`, ki vrne vsoto kvadratov števk
# *tromestnega* števila `n`.
# 
#     >>> vsota_kvadratov_stevk(123)
#     14
# =============================================================================
def vsota_kvadratov_stevk(n):
    e=n%10
    d=n//10%10
    s=n//100
    return e**2+ d**2 + s**2

vsota_kvadratov_stevk(123)


# =====================================================================@000925=
# 2. podnaloga
# Sestavite funkcijo `obrat(n)`, ki vrne število, ki ga dobimo, če številu `n`
# zamenjamo števki na mestu enic in stotic.
# 
#     >>> obrat(123)
#     321
# =============================================================================
def obrat(n):
    e = n % 10
    d = n // 10 % 10
    s = n // 100
    return e*100 + d*10 + s

obrat(123)


# =====================================================================@000926=
# 3. podnaloga
# Da bi pri obdelavi podatkov lahko prepoznali morebitne napake, številske
# podatke pogosto opremimo s kontrolnimi števkami. Eden takšnih podatkov je
# sklic (referenca) po standardu SI12, ki ga uporabljamo pri plačevanju s
# položnicami UPN. Sklic zapišemo kot 13-mestno število, pri čemer je prvih 12
# števk poljubnih, zadnja (trinajsta) pa je kontrolna, torej izračunana iz
# prejšnjih, in nam služi za preverjanje, ali je pri branju podatkov s položnice
# bilo vse v redu.
# 
# Kontrolno števko za dano 12-mestno število izračunamo tako, da števke od desne
# proti levi pomnožimo z zaporednimi števili 2, 3, 4, … (enice torej pomnožimo z
# 2, desetice s 3, stotice s 4, …). Dobljene produkte seštejemo, nato izračunamo
# ostanek, ki ga da dobljena vsota pri deljenju z 11, in ta ostanek odštejemo od
# 11. Dobimo število med 1 in 11. Če je to število manjše od 10, je to že kar
# iskana kontrolna števka, sicer pa je kontrolna števka enaka 0.
# 
# Sestavite funkcijo `dodaj_kontrolno_stevko(sklic)`, ki za 12-mestno število
# `sklic` vrne 13-mestno število s pripadajočo kontrolno števko.
# 
#     >>> dodaj_kontrolno_stevko(265195368523)
#     2651953685235
# =============================================================================

def dodaj_kontrolno_stevko(sklic):
    a= sklic % 10
    b= sklic // 10 % 10
    c=sklic // 100 % 10
    d=sklic // 1000 % 10
    e=sklic // 10000 % 10
    f=sklic // 100000 % 10
    g=sklic // 1000000 % 10
    h=sklic // 10000000 % 10
    i=sklic // 100000000 % 10
    j=sklic // 1000000000 % 10
    k=sklic // 10000000000 % 10
    l=sklic // 100000000000 % 10

    x= 11-((a*2 + b*3 + c*4 + d*5 + e*6 + f*7 + g*8 + h*9 + i*10 + j*11 + k*12 + l*13)%11)
    if x > 9:
        return sklic*10
    else:
        return sklic*10+x













































































































# ============================================================================@

'Če vam Python sporoča, da je v tej vrstici sintaktična napaka,'
'se napaka v resnici skriva v zadnjih vrsticah vaše kode.'

'Kode od tu naprej NE SPREMINJAJTE!'


















































import io, json, os, re, sys, shutil, traceback, urllib.error, urllib.request
from contextlib import contextmanager


class Check:
    @staticmethod
    def has_solution(part):
        return part['solution'].strip() != ''

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part['valid'] = True
            part['feedback'] = []
            part['secret'] = []
        Check.current_part = None
        Check.part_counter = None

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]
        return Check.has_solution(Check.current_part)

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part['feedback'].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part['valid'] = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6):
        if type(x) is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            return x if x else 0.0
        elif type(x) is complex:
            return complex(Check.clean(x.real, digits), Check.clean(x.imag, digits))
        elif type(x) is list:
            return list([Check.clean(y, digits) for y in x])
        elif type(x) is tuple:
            return tuple([Check.clean(y, digits) for y in x])
        elif type(x) is dict:
            return sorted([(Check.clean(k, digits), Check.clean(v, digits)) for (k, v) in x.items()])
        elif type(x) is set:
            return sorted([Check.clean(y, digits) for y in x])
        else:
            return x

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = clean or Check.clean
        Check.current_part['secret'].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env={}):
        local_env = locals()
        local_env.update(env)
        clean = clean or Check.clean
        actual_result = eval(expression, globals(), local_env)
        if clean(actual_result) != clean(expected_result):
            Check.error('Izraz {0} vrne {1!r} namesto {2!r}.',
                        expression, actual_result, expected_result)
            return False
        else:
            return True

    @staticmethod
    def run(statements, expected_state, clean=None, env={}):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        s = {}
        s.update(env)
        clean = clean or Check.clean
        exec(code, globals(), s)
        errors = []
        for (x, v) in expected_state.items():
            if x not in s:
                errors.append('morajo nastaviti spremenljivko {0}, vendar je ne'.format(x))
            elif clean(s[x]) != clean(v):
                errors.append('nastavijo {0} na {1!r} namesto na {2!r}'.format(x, s[x], v))
        if errors:
            Check.error('Ukazi\n{0}\n{1}.', statements,  ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        with open(filename, 'w', encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part['feedback'][:]
        yield
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n    '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}', filename, '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    @contextmanager
    def input(content, encoding=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part['feedback'][:]
        sys.stdin = io.StringIO('\n'.join(content))
        try:
            yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n  '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}', '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    def out_file(filename, content, encoding=None):
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error('Izhodna datoteka {0}\n je enaka{1}  namesto:\n  {2}', filename, (line_width - 7) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def output(expression, content):
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            def visible_input(prompt):
                inp = input(prompt)
                print(inp)
                return inp
            exec(expression, {'input': visible_input})
        finally:
            output = sys.stdout.getvalue().strip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal:
            return True
        else:
            Check.error('Program izpiše{0}  namesto:\n  {1}', (line_width - 13) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ['\n']
        else:
            expected_lines += (actual_len - expected_len) * ['\n']
        equal = True
        line_width = max(len(actual_line.rstrip()) for actual_line in actual_lines + ['je enaka'])
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append('{0} {1} {2}'.format(out.ljust(line_width), '|' if out == given else '*', given))
        return equal, diff, line_width

    @staticmethod
    def generator(expression, expected_values, should_stop=False, further_iter=0, env={}, clean=None):
        from types import GeneratorType
        local_env = locals()
        local_env.update(env)
        clean = clean or Check.clean
        gen = eval(expression, globals(), local_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error("Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                                iteration, expression, actual_value, expected_value)
                    return False
            for _ in range(further_iter):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False
        
        if should_stop:
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not Check.has_solution(part):
                print('{0}. podnaloga je brez rešitve.'.format(i + 1))
            elif not part['valid']:
                print('{0}. podnaloga nima veljavne rešitve.'.format(i + 1))
            else:
                print('{0}. podnaloga ima veljavno rešitev.'.format(i + 1))
            for message in part['feedback']:
                print('  - {0}'.format('\n    '.join(message.splitlines())))


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding='utf-8') as f:
            source = f.read()
        part_regex = re.compile(
            r'# =+@(?P<part>\d+)=\n'  # beginning of header
            r'(#( [^\n]*)?\n)+'       # description
            r'# =+\n'                 # end of header
            r'(?P<solution>.*?)'      # solution
            r'(?=\n# =+@)',           # beginning of next part
            flags=re.DOTALL | re.MULTILINE
        )
        parts = [{
            'part': int(match.group('part')),
            'solution': match.group('solution')
        } for match in part_regex.finditer(source)]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]['solution'] = parts[-1]['solution'].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = '{0}.{1}'.format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    'part': part['part'],
                    'solution': part['solution'],
                    'valid': part['valid'],
                    'secret': [x for (x, _) in part['secret']],
                    'feedback': json.dumps(part['feedback']),
                }
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode('utf-8')
        headers = {
            'Authorization': token,
            'content-type': 'application/json'
        }
        request = urllib.request.Request(url, data=data, headers=headers)
        response = urllib.request.urlopen(request)
        return json.loads(response.read().decode('utf-8'))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response['attempts']:
            part['feedback'] = json.loads(part['feedback'])
            updates[part['part']] = part
        for part in old_parts:
            valid_before = part['valid']
            part.update(updates.get(part['part'], {}))
            valid_after = part['valid']
            if valid_before and not valid_after:
                wrong_index = response['wrong_indices'].get(str(part['part']))
                if wrong_index is not None:
                    hint = part['secret'][wrong_index][1]
                    if hint:
                        part['feedback'].append('Namig: {}'.format(hint))


    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        try:
            Check.equal('vsota_kvadratov_stevk(123)', 14)
            Check.equal('vsota_kvadratov_stevk(998)', 226)
            Check.equal('vsota_kvadratov_stevk(111)', 3)
            Check.equal('vsota_kvadratov_stevk(999)', 243)
            Check.equal('vsota_kvadratov_stevk(321)', 14)
            Check.equal('vsota_kvadratov_stevk(714)', 66) and \
            Check.equal('vsota_kvadratov_stevk(417)', 66) and \
            Check.equal('vsota_kvadratov_stevk(471)', 66) and \
            Check.equal('vsota_kvadratov_stevk(174)', 66) and \
            Check.equal('vsota_kvadratov_stevk(741)', 66) and \
            Check.equal('vsota_kvadratov_stevk(147)', 66)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            Check.equal('obrat(123)', 321)
            Check.equal('obrat(998)', 899)
            Check.equal('obrat(111)', 111)
            Check.equal('obrat(999)', 999)
            Check.equal('obrat(321)', 123)
            Check.equal('obrat(714)', 417) and \
            Check.equal('obrat(417)', 714) and \
            Check.equal('obrat(471)', 174) and \
            Check.equal('obrat(174)', 471) and \
            Check.equal('obrat(741)', 147) and \
            Check.equal('obrat(147)', 741)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            Check.equal('dodaj_kontrolno_stevko(265195368523)', 2651953685235)
            Check.equal('dodaj_kontrolno_stevko(309763415292)', 3097634152921)
            Check.equal('dodaj_kontrolno_stevko(790490603490)', 7904906034909)
            Check.equal('dodaj_kontrolno_stevko(957800321625)', 9578003216256)
            Check.equal('dodaj_kontrolno_stevko(958811067176)', 9588110671763)
            Check.equal('dodaj_kontrolno_stevko(967881885905)', 9678818859054)
            Check.equal('dodaj_kontrolno_stevko(948946641471)', 9489466414712)
            Check.equal('dodaj_kontrolno_stevko(641602340292)', 6416023402920)
            Check.equal('dodaj_kontrolno_stevko(948666700540)', 9486667005400)
            Check.equal('dodaj_kontrolno_stevko(121679652819)', 1216796528197)
            Check.equal('dodaj_kontrolno_stevko(493557029514)', 4935570295148)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    print('Shranjujem rešitve na strežnik... ', end="")
    try:
        url = 'https://www.projekt-tomo.si/api/attempts/submit/'
        token = 'Token 98a268926b7e7106ad9fce1100b8d448a5be8f6d'
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        print('PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE! Poskusite znova.')
    else:
        print('Rešitve so shranjene.')
        update_attempts(Check.parts, response)
        if 'update' in response:
            print("Posodabljam datoteko... ", end="")
            backup_filename = backup(filename)
            r = urlopen(response['update'])
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(r.read().decode('utf-8'))
            print("Stara datoteka je preimenovana v {0}.".format(os.path.basename(backup_filename)))
            print("Če se datoteka v urejevalniku ni osvežila, jo zaprite ter ponovno odprite.")
    Check.summarize()

_validate_current_file()
