import re

# graphs colors
instance_colors = {"a1.large-1": "#cc7a00",
                  "a1.large-2": "#cc7a00",
                  "a1.xlarge-1": "#ffad33",
                  "m5.large-1": "#ffd699",
                  "m5.large-2": "#ffd699",
                  "m5.xlarge-1": "#ffebcc",
                  "A2-1": "#0052cc",
                  "A2-2": "#0052cc",
                  "A4-1": "#3385ff",
                  "B2MS-1": "#99c2ff",
                  "B2MS-2": "#99c2ff",
                  "B4MS-1": "#cce0ff",
                  "e2-t1-1": "#cc2900",
                  "e2-t1-2": "#cc2900",
                  "e2-t2-1": "#ff5c33",
                  "n1-t1-1": "#ffad99",
                  "n1-t1-2": "#ffad99",
                  "n1-t2-1": "#ffd6cc",
                  "T1-1": "#33cc00",
                  "T1-2": "#33cc00",
                  "T2-1": "#66ff33",
                  "T3-1": "#b3ff99",
                  "T3-2": "#b3ff99",
                  "T4-1": "#d9ffcc"}

# bench alias
bench_alias = {"817407f47eeb0c43023a5487985867a64960c778": "NETB 1",
"cbadb796cb57922b59801d6993b79d8ce3bcf674": "DISKB LAT",
"5b6cb427d11dfdd876e2dfedeb8039bbb2bf00b8": "CPU SHA256",
"277604812f42491cbabe59d60001aaffc925c2b5": "CPU BZIP2",
"e9657314c54bc9cc01cbe5d4e606c6d882c1d559": "CPU AES",
"eb556387684749126951d10bf3530e6636d9a25e": "DISK SEQ W",
"b08b0f666899016c90c3eb06dc2dc78c86db05fe": "NET 1",
"4f9036957f18874f519316848e75bed92f7ec50a": "NET 2",
"96097006f73de91de5d6d52b169b3c0122d8cc40": "NET 3",
"6b15fec1cbb97aa537c29c8bb0adff3235a505e3": "NET 4",
"4b7ccf0064e0a3ebfe54a6a139b35958a896593b": "NET 5",
"83504705835a4243a1c3958b31dcd54d72246b7e": "NETB 2",
"7d7b07646009b4a87b48c9519d7a95a5a994ba93": "APPB",
"09b85683be2ff3589454eceefca9a640e3fb6508": "CPU DUR",
"6157345de84637c53718d2ad44c67ee65c6b3dbd": "DISKB THR",
"cd6051f39616e101ee3586810d90aabc4703711b": "CPU EVENTS",
"4f1601a2fee6f318db2255d8d70480bcd32114bb": "CPU LAT",
"770e3a2ca8b8a0765a10a2afdb6a476e7e4f8e6c": "DISK FILE R",
"5b6d62d2c3e75fa54f053717e103d742ca2e7ded": "DISK FILE W",
"76a291182ae2a33c1a8bc6baf134a35afd2e78c6": "DISK FILE F",
"871c7e28e1d90a5faead69ee6c87b09f18bc04c6": "DISK THR R",
"c5f1a6b81b73cea76082bc1c2fa0af1b06c4733e": "DISK THR W",
"6b10bb7744ab058af8c49896ff2de9433f360d05": "DISK LAT",
"4ff72d794db9bfc16f363cb21933f7860dc2a796": "MEM OPS",
"11d4515d916b810e82d25d90d9cc29181d2832ce": "MEM SPEED",
"4fbaaef78c368efc3613e57f57b559876121c0ef": "MEM LAT",
"a9877955225656b989fcfeea050078e6b2639ced": "CPU TH LAT",
"4edcdef29160f30a36d7e070b8267674e810f5f0": "DISK SEEK",
"c0e258974e33e7600e1c07c98746943176e8ff1c": "DISK SEQ R",
"56d916334c55408ad318eff68579a8b585569a4b": "NETB 3"}

def get_instance_color(s):
    if s in instance_colors:
        return instance_colors[s]
    else:
        return "#a89984"

def get_bench_alias(s):
    if s in bench_alias:
        return bench_alias[s]
    else:
        return s

def get_valid_filename(s):
    s = str(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)

def get_filename(provider, bench_alias, key, instance=None):
    if instance:
      return provider + "_" + get_valid_filename(instance) + "_" + get_valid_filename(bench_alias) + "_" + str(key)[0:5]
    else:
      return provider + "_" + get_valid_filename(bench_alias) + "_" + str(key)[0:5]
    
# helpers
def plot_dates(x, y, label=None, suptitle=None):
    fig, ax = plt.subplots()
    if suptitle:
        fig.suptitle(suptitle)
    ax.plot(x, y, label=label)
    ax.xaxis.set_major_formatter(date_formatter)
    fig.autofmt_xdate()
    plt.grid(True, linewidth=0.3, linestyle='-')
    plt.show()
    plt.close()
    
def plotly_dates(x, y, label=None, suptitle=None):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=label))
    fig.update_layout(autosize=False)
    fig.update_yaxes(automargin=False)
    fig.show()

def change_uom(uom):
  return uom.replace("s", "sec")