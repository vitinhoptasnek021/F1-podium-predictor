import argparse
import fastf1
from f1_predictor.config import CACHE_DIR, DATA_RAW

def collect_race(year: int, gp: str, session_code: str = "R"):
    fastf1.Cache.enable_cache(str(CACHE_DIR))
    session = fastf1.get_session(year, gp, session_code)
    session.load(telemetry=False, laps=False, weather=False)

    results = session.results
    columns = ["Abbreviation", "FullName", "TeamName",
               "GridPosition", "Position", "Points", "Status"]
    df = results[[c for c in columns if c in results.columns]].copy()
    df["year"] = year
    df["event"] = gp
    df["session"] = session_code

    output = DATA_RAW / f"f1_{year}_{gp.lower().replace(' ', '_')}_{session_code.lower()}.csv"
    df.to_csv(output, index=False)
    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--gp", required=True)
    parser.add_argument("--session", default="R")
    args = parser.parse_args()
    print("Arquivo salvo em:", collect_race(args.year, args.gp, args.session))
