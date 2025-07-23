# Ініціювання виключень при роботі з файлом

import sys

fsum = None
try:
    cf = open("content.txt")
    while True:
        cline = cf.readline()
        if len(cline) == 0: break
        cline = list(cline.split())
        for fname in cline:
            try:
                f = open(fname, encoding="utf-8")
                try:
                    lines = f.readlines()
                    for line in lines:
                        line = list(line.split())
                        for num in line:
                            try:
                                if fsum is None: fsum = 0
                                fsum += float(num)

                            except ValueError:
                                continue

                except EOFError:
                    break
                except ValueError:
                    continue
                else:
                    pass
                finally:
                    print('Файл "%s" опрацьовано.' % fname)

                f.close()

            except FileNotFoundError as fn:
                print("Файл не знайдено:", fn.filename)
            except IOError as err:
                print("Помилка вводу/виводу (%s): %s" % (err.errno, err.strerror))
            except OSError as e:
                print("Помилка ОС")
                raise e
            except:
                print("Несподівана помилка:", sys.exc_info()[0])
                raise

    cf.close()

except FileNotFoundError as fn:
    print("Файл не знайдено:", fn.filename)
except IOError as err:
    print("Помилка вводу/виводу (%s): %s" % (err.errno, err.strerror))
except OSError as e:
    print("Помилка ОС")
    raise e
except:
    print("Несподівана помилка:", sys.exc_info()[0])
    raise

print("\nСума даних з файлів =", fsum)
