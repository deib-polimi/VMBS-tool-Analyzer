import re

def parser_sysbench(raw_data, print_errors=True):
    parsing_errors = 0
    sys_res = []
    cpu_tests = [(r"events per second:\s*([0-9.]*)", "cpu: events per second", "events/s"),
                (r"avg:\s*([0-9.]*)", "cpu: avg latency", "ms")]
    fileio_tests = [(r"reads\/s:\s*([0-9.]*)", "fileio: fileop - read", "reads/s"),
                    (r"writes\/s:\s*([0-9.]*)", "fileio: fileop - write", "writes/s"),
                    (r"fsyncs\/s:\s*([0-9.]*)", "fileio: fileop - fsync", "fsyncs/s"),
                    (r"read, MiB\/s:\s*([0-9.]*)", "fileio: throughput - read", "MiB/s"),
                    (r"written, MiB\/s:\s*([0-9.]*)", "fileio: throughput - write", "MiB/s"),
                    (r"avg:\s*([0-9.]*)", "fileio: avg latency", "ms")]
    memory_tests = [#(r"([0-9.,]*) per second", "memory: totalops per second", "ops/s"),
                    (r"([0-9.,]*) MiB\/sec", "memory: speed", "MiB/s"),
                    (r"avg:\s*([0-9.]*)", "memory: avg latency", "ms")]
    threads_tests = [(r"avg:\s*([0-9.]*)", "threads: avg latency", "ms")]
    for benchmark in [("cpu", cpu_tests), ("fileio", fileio_tests),
                      ("memory", memory_tests), ("threads", threads_tests)]:
        r_data = raw_data[benchmark[0]]
        tests = benchmark[1]
        for test in tests:
            try:
                match = re.findall(test[0], r_data, re.MULTILINE)
                res = float(match[0].replace(",", "."))
                name = test[1]
                unit = test[2]
                sys_res.append({"unit": unit, "value": res, "name": name})
            except Exception as e:
                parsing_errors += 1
                if print_errors:
                    print("error: sysbench: " + str(e))
    return sys_res, len(sys_res), parsing_errors

def parser_simplecpu(raw_data, print_errors=True):
    return [{"unit": "s", "value": raw_data, "name": "mean duration"}], 1, 0

def parser_download(raw_data, print_errors=True):
    # extract size and time
    regex = r"Downloaded\s([0-9]*)[a-z\s]*([0-9.,]*)"
    match = re.findall(regex, raw_data, re.MULTILINE)
    size = float(match[0][0])/1000/1000
    time = float(match[0][1].replace(",", "."))
    return [{"unit": "MB/s", "value": round(size/time, 2), "name": "speed"}], 1, 0

def parser_dd(raw_data, print_errors=True):
    # extract speed
    regex = r"s,\s([0-9.,]*)\s[a-zA-Z]*\/s"
    match = re.findall(regex, raw_data, re.MULTILINE)
    speed = float(str(match[0]).replace(",", "."))
    return [{"unit": "MB/s", "value": speed, "name": "speed"}], 1, 0

def parser_web_benchmark(raw_data, print_errors=True):
    regex = r"Requests/sec:\s*([0-9.]*)"
    match = re.findall(regex, raw_data, re.MULTILINE)
    speed = float(str(match[0]).replace(",", "."))
    return [{"unit": "req/s", "value": speed, "name": "requests per second"}], 1, 0

def parser_nench(raw_data, print_errors=True):
    parsing_errors = 0
    # cpu
    cpu_res = []
    for cpu_test in ["SHA256", "bzip2", "AES"]:
        regex = re.escape(cpu_test) + ".*\n\s*([0-9,.]*) ([a-z]*)"
        try:
            match = re.findall(regex, raw_data, re.MULTILINE)
            res = float(str(match[0][0]).replace(",", "."))
            unit = str(match[0][1])
            cpu_res.append({"unit": unit, "value": res, "name": "cpu - " + cpu_test})
        except Exception as e:
            parsing_errors += 1
            if print_errors:
                print("error: nench - cpu: " + str(e))
    # ioping
    ioping_res = []
    seekrate = (r"min\/avg\/max\/mdev = [0-9a-z.\s]*\/ ([0-9.]*) ([a-z]*)", "ioping: avg seek rate")
    srs = (r"generated.*iops. ([0-9.]*) (.*)", "ioping: sequential read speed")
    for ioping in [seekrate, srs]:
        regex = ioping[0]
        try:
            match = re.findall(regex, raw_data, re.MULTILINE)
            res = float(str(match[0][0]).replace(",", "."))
            unit = str(match[0][1])
            ioping_res.append({"unit": unit, "value": res, "name": ioping[1]})
        except Exception as e:
            parsing_errors += 1
            if print_errors:
                print("error: nench - ioping: " + str(e))
    # dd
    try:
        dd_res = []
        regex = r"average:\s*([0-9.]*) ([a-zA-Z\/]*)$"
        match = re.findall(regex, raw_data, re.MULTILINE)
        res = float(str(match[0][0]).replace(",", "."))
        unit = str(match[0][1])
        dd_res.append({"unit": unit, "value": res, "name": "dd: avg sequential write speed"})
    except Exception as e:
        parsing_errors += 1
        if print_errors:
            print("error: nench - dd: " + str(e))
    # speed test
    speed_res = []
    for speed_test in ["Cachefly CDN", "Leaseweb (NL)", "Softlayer DAL (US)", "Online.net (FR)", "OVH BHS (CA)"]:
        regex = re.escape(speed_test) + ":\s*([0-9.]*) ([a-zA-Z\/]*)"
        try:
            match = re.findall(regex, raw_data, re.MULTILINE)
            res = float(str(match[0][0]).replace(",", "."))
            unit = str(match[0][1])
            speed_res.append({"unit": unit, "value": res, "name": "net speed - " + speed_test})
        except Exception as e:
            parsing_errors += 1
            if print_errors:
                print("error: nench - speed test: " + str(e))
    return cpu_res + ioping_res + dd_res + speed_res, len(cpu_res + ioping_res + dd_res + speed_res), parsing_errors

def parser_aibenchmark(raw_data, print_errors=True):
    ai_res = []
    if raw_data["ai_score"]:
        ai_res.append({"unit": "score", "value": raw_data["ai_score"], "name": "ai score"})
    if raw_data["inference_score"]:
        ai_res.append({"unit": "score", "value": raw_data["inference_score"], "name": "inference score"})
    if raw_data["training_score"]:
        ai_res.append({"unit": "score", "value": raw_data["training_score"], "name": "training score"})
    return ai_res, len(ai_res), 0

def htr(unit):
    if unit == "s" or unit == "seconds" or unit =="ms" or unit == "us":
        return "LIB"
    return "HIB"

benchmark_extractors = {"download": parser_download,
                        "dd": parser_dd,
                        "web-benchmark": parser_web_benchmark,
                        "nench-benchmark": parser_nench,
                        "sys-benchmark": parser_sysbench,
                        "simple-cpu": parser_simplecpu,
                        "ai-benchmark": parser_aibenchmark}

