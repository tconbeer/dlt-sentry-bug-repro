import dlt

if __name__ == "__main__":
    p = dlt.pipeline(destination="duckdb", pipeline_name="pipe")
    print(p.run([1,2,3], table_name="numbers"))