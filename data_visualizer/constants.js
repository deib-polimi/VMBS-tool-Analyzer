const providers = ["aws", "azure", "gcp", "egi"]
const graphTypes = ["time", "mean", "delta", "pqi", "execution"]
const benchmarks = [
    {
        "id": "817407f47eeb0c43023a5487985867a64960c778",
        "bench_name": "download",
        "extracted_name": "speed"
    },
    {
        "id": "56d916334c55408ad318eff68579a8b585569a4b",
        "bench_name": "download",
        "extracted_name": "speed"
    },
    {
        "id": "cbadb796cb57922b59801d6993b79d8ce3bcf674",
        "bench_name": "dd",
        "extracted_name": "speed"
    },
    {
        "id": "5b6cb427d11dfdd876e2dfedeb8039bbb2bf00b8",
        "bench_name": "nench-benchmark",
        "extracted_name": "cpu - SHA256"
    },
    {
        "id": "277604812f42491cbabe59d60001aaffc925c2b5",
        "bench_name": "nench-benchmark",
        "extracted_name": "cpu - bzip2"
    },
    {
        "id": "e9657314c54bc9cc01cbe5d4e606c6d882c1d559",
        "bench_name": "nench-benchmark",
        "extracted_name": "cpu - AES"
    },
    {
        "id": "eb556387684749126951d10bf3530e6636d9a25e",
        "bench_name": "nench-benchmark",
        "extracted_name": "dd: avg sequential write speed"
    },
    {
        "id": "b08b0f666899016c90c3eb06dc2dc78c86db05fe",
        "bench_name": "nench-benchmark",
        "extracted_name": "net speed - Cachefly CDN"
    },
    {
        "id": "4f9036957f18874f519316848e75bed92f7ec50a",
        "bench_name": "nench-benchmark",
        "extracted_name": "net speed - Leaseweb (NL)"
    },
    {
        "id": "96097006f73de91de5d6d52b169b3c0122d8cc40",
        "bench_name": "nench-benchmark",
        "extracted_name": "net speed - Softlayer DAL (US)"
    },
    {
        "id": "6b15fec1cbb97aa537c29c8bb0adff3235a505e3",
        "bench_name": "nench-benchmark",
        "extracted_name": "net speed - Online.net (FR)"
    },
    {
        "id": "4b7ccf0064e0a3ebfe54a6a139b35958a896593b",
        "bench_name": "nench-benchmark",
        "extracted_name": "net speed - OVH BHS (CA)"
    },
    {
        "id": "83504705835a4243a1c3958b31dcd54d72246b7e",
        "bench_name": "download",
        "extracted_name": "speed"
    },
    {
        "id": "7d7b07646009b4a87b48c9519d7a95a5a994ba93",
        "bench_name": "web-benchmark",
        "extracted_name": "requests per second"
    },
    {
        "id": "09b85683be2ff3589454eceefca9a640e3fb6508",
        "bench_name": "simple-cpu",
        "extracted_name": "mean duration"
    },
    {
        "id": "6157345de84637c53718d2ad44c67ee65c6b3dbd",
        "bench_name": "dd",
        "extracted_name": "speed"
    },
    {
        "id": "cd6051f39616e101ee3586810d90aabc4703711b",
        "bench_name": "sys-benchmark",
        "extracted_name": "cpu: events per second"
    },
    {
        "id": "4f1601a2fee6f318db2255d8d70480bcd32114bb",
        "bench_name": "sys-benchmark",
        "extracted_name": "cpu: avg latency"
    },
    {
        "id": "770e3a2ca8b8a0765a10a2afdb6a476e7e4f8e6c",
        "bench_name": "sys-benchmark",
        "extracted_name": "fileio: fileop - read"
    },
    {
        "id": "5b6d62d2c3e75fa54f053717e103d742ca2e7ded",
        "bench_name": "sys-benchmark",
        "extracted_name": "fileio: fileop - write"
    },
    {
        "id": "76a291182ae2a33c1a8bc6baf134a35afd2e78c6",
        "bench_name": "sys-benchmark",
        "extracted_name": "fileio: fileop - fsync"
    },
    {
        "id": "871c7e28e1d90a5faead69ee6c87b09f18bc04c6",
        "bench_name": "sys-benchmark",
        "extracted_name": "fileio: throughput - read"
    },
    {
        "id": "c5f1a6b81b73cea76082bc1c2fa0af1b06c4733e",
        "bench_name": "sys-benchmark",
        "extracted_name": "fileio: throughput - write"
    },
    {
        "id": "6b10bb7744ab058af8c49896ff2de9433f360d05",
        "bench_name": "sys-benchmark",
        "extracted_name": "fileio: avg latency"
    },
    {
        "id": "11d4515d916b810e82d25d90d9cc29181d2832ce",
        "bench_name": "sys-benchmark",
        "extracted_name": "memory: speed"
    },
    {
        "id": "4fbaaef78c368efc3613e57f57b559876121c0ef",
        "bench_name": "sys-benchmark",
        "extracted_name": "memory: avg latency"
    },
    {
        "id": "a9877955225656b989fcfeea050078e6b2639ced",
        "bench_name": "sys-benchmark",
        "extracted_name": "threads: avg latency"
    },
    {
        "id": "4edcdef29160f30a36d7e070b8267674e810f5f0",
        "bench_name": "nench-benchmark",
        "extracted_name": "ioping: avg seek rate"
    },
    {
        "id": "c0e258974e33e7600e1c07c98746943176e8ff1c",
        "bench_name": "nench-benchmark",
        "extracted_name": "ioping: sequential read speed"
    }
]
const machines = {
    "aws": ["aws_a1.large-1", "aws_a1.large-2", "aws_a1.xlarge-1", "aws_m5.large-1", "aws_m5.large-2", "aws_m5.xlarge-1"],
    "azure": ["azure_A2-1", "azure_A2-2", "azure_A4-1", "azure_B2MS-1", "azure_B2MS-2", "azure_B4MS-1"],
    "egi": ["egi_T1-1", "egi_T1-2", "egi_T2-1", "egi_T3-1", "egi_T3-2", "egi_T4-1"],
    "gcp": ["gcp_e2-t1-1", "gcp_e2-t1-2", "gcp_e2-t2-1", "gcp_n1-t1-1", "gcp_n1-t1-2", "gcp_n1-t2-1"]
}

const bench = {
    "7d7b07646009b4a87b48c9519d7a95a5a994ba93": "APPB", 
    "e9657314c54bc9cc01cbe5d4e606c6d882c1d559": "CPU AES", 
    "277604812f42491cbabe59d60001aaffc925c2b5": "CPU BZIP2", 
    "09b85683be2ff3589454eceefca9a640e3fb6508": "CPU DUR", 
    "cd6051f39616e101ee3586810d90aabc4703711b": "CPU EVENTS", 
    "4f1601a2fee6f318db2255d8d70480bcd32114bb": "CPU LAT", 
    "5b6cb427d11dfdd876e2dfedeb8039bbb2bf00b8": "CPU SHA256", 
    "a9877955225656b989fcfeea050078e6b2639ced": "CPU TH LAT", 
    "76a291182ae2a33c1a8bc6baf134a35afd2e78c6": "DISK FILE F", 
    "770e3a2ca8b8a0765a10a2afdb6a476e7e4f8e6c": "DISK FILE R", 
    "5b6d62d2c3e75fa54f053717e103d742ca2e7ded": "DISK FILE W", 
    "6b10bb7744ab058af8c49896ff2de9433f360d05": "DISK LAT", 
    "4edcdef29160f30a36d7e070b8267674e810f5f0": "DISK SEEK", 
    "c0e258974e33e7600e1c07c98746943176e8ff1c": "DISK SEQ R", 
    "eb556387684749126951d10bf3530e6636d9a25e": "DISK SEQ W", 
    "871c7e28e1d90a5faead69ee6c87b09f18bc04c6": "DISK THR R", 
    "c5f1a6b81b73cea76082bc1c2fa0af1b06c4733e": "DISK THR W", 
    "cbadb796cb57922b59801d6993b79d8ce3bcf674": "DISKB LAT", 
    "6157345de84637c53718d2ad44c67ee65c6b3dbd": "DISKB THR", 
    "4fbaaef78c368efc3613e57f57b559876121c0ef": "MEM LAT", 
    "11d4515d916b810e82d25d90d9cc29181d2832ce": "MEM SPEED", 
    "b08b0f666899016c90c3eb06dc2dc78c86db05fe": "NET 1", 
    "4f9036957f18874f519316848e75bed92f7ec50a": "NET 2", 
    "96097006f73de91de5d6d52b169b3c0122d8cc40": "NET 3", 
    "6b15fec1cbb97aa537c29c8bb0adff3235a505e3": "NET 4", 
    "4b7ccf0064e0a3ebfe54a6a139b35958a896593b": "NET 5", 
    "817407f47eeb0c43023a5487985867a64960c778": "NETB 1", 
    "83504705835a4243a1c3958b31dcd54d72246b7e": "NETB 2", 
    "56d916334c55408ad318eff68579a8b585569a4b": "NETB 3"
}