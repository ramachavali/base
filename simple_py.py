#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser(description = "Gather and summarize daily SSC report files")

parser.add_argument("--usd-jpy", type = float, default = 108.98, help = "how many jpy to make 1 usd (default %(default)s)")
parser.add_argument("--max-jobs", type = int, default = -1, help = "max jobs to run at once (default: ncpus)")
parser.add_argument("--out-dir", type = str, help = "directory for output csv files")
parser.add_argument("begin_date", type = str, help = "beginning date (inclusive)")
parser.add_argument("end_date", type = str, help = "ending date (exclusive)")

args = parser.parse_args()

begin_date = args.begin_date
end_date = args.end_date
max_jobs = args.max_jobs
out_dir = args.out_dir

def gather_filenames(calendar, begin_date, end_date, pattern):
    cmd = ["get_daily_names", calendar, begin_date, end_date, pattern]
    return subprocess.check_output(cmd, universal_newlines = True).strip().split()

def read_file(filename):
    f = open(filename)
    result = f.read().strip()
    f.close()
    return result

def print_results(filename, results):
    ps = jxtp.java.io.PrintStream(jxtp.xtp.util.OutputFile.of(filename).get_output_stream())
    for line in results:
        ps.println(line)
    ps.close()

# TODO: make this whole thing a function instead of inline
for pool, pcfg in pools.items():
    pattern = "s3://bfc-archive/reports/in/ssc/{SLASHY_DATE}/%s_pos_eod_{COMPACT_DATE}.txt.gz" % (pcfg["tag"])
    filenames = gather_filenames(pcfg["calendar"], max(begin_date, pcfg["begin_date"]), end_date, pattern)
    cfg = xmd.Configuration()
    cfg.env["MUL"] = pcfg["to_usd_f"]
    result_files = []
    for fn in filenames:
        bn = os.path.basename(fn) + ".txt"
        rn = os.path.join(cache_dir, pool, bn)
        cfg.targets[rn] = xmd.OutputOf("exec_w_input ${1} summarize_ssc_report -O , -m ${MUL}", [fn])
        result_files += [rn]
    r = xmd.Runner()
    r.max_jobs = max_jobs
    r.output_type = "full"
    r.run(cfg)

    print(pool)
    result = ["date,daily,mtd,ytd"]
    for fn in sorted(result_files):
        result += [read_file(fn)]
    print_results("stdout", result)

    if out_dir:
        out_file = os.path.join(out_dir, "ssc_%s.csv" % (pool))
        print_results(out_file, result)

