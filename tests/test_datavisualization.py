import pandas as pd
from gitpraise.datavisualization import DataVisualization
from pdfminer.high_level import extract_text

# Test processDataType txt type with empty results input
def test_processDatatype_txt_with_empty_results():
        final_df = pd.DataFrame()
        format = "txt"
        results = [None, None]
        expected_df = pd.DataFrame()
        expected_string = ""

        dv = DataVisualization()
        actual_df, actual_string = dv.processDatatype(final_df, format, results)

        pd.testing.assert_frame_equal(actual_df, expected_df)
        assert actual_string == expected_string

# Test processDataType csv type with empty results input
def test_processDatatype_csv_with_empty_results():
        final_df = pd.DataFrame()
        format = "csv"
        results = [None, None]
        expected_df = pd.DataFrame()
        expected_string = ""

        dv = DataVisualization()
        actual_df, actual_string = dv.processDatatype(final_df, format, results)

        pd.testing.assert_frame_equal(actual_df, expected_df)
        assert actual_string == expected_string

# Test processDataType pdf type with empty results input
def test_processDatatype_pdf_with_empty_results():
        final_df = pd.DataFrame()
        format = "pdf"
        results = [None, None]
        expected_df = pd.DataFrame()
        expected_string = ""

        dv = DataVisualization()
        actual_df, actual_string = dv.processDatatype(final_df, format, results)

        pd.testing.assert_frame_equal(actual_df, expected_df)
        assert actual_string == expected_string

# Test processDataType txt type with sample result data
def test_processDatatype_txt_with_valid_results():
        final_df = pd.DataFrame()
        format = "txt"
        results = [
            {"type": "linecontributions", "filename": "file1", "data": pd.DataFrame({
                "commithash": ["12345", "67890"],
                "author": ["Alice", "Bob"],
                "date": ["2022-01-01", "2022-01-02"],
                "linenum": [1, 2],
                "content": ["line 1", "line 2"]
            })},
            {"type": "linecontributions", "filename": "file2", "data": pd.DataFrame({
                "commithash": ["54321", "09876"],
                "author": ["Alice", "Charlie"],
                "date": ["2022-01-03", "2022-01-04"],
                "linenum": [1, 2],
                "content": ["line 1", "line 2"]
            })}
        ]
        expected_df = pd.DataFrame({
        })
        expected_string = "file1\n 12345  Alice  2022-01-01 1)  line 1\n 67890    Bob  2022-01-02 2)  line 2\n\nfile2\n 54321    Alice  2022-01-03 1)  line 1\n 09876  Charlie  2022-01-04 2)  line 2\n\n"

        dv = DataVisualization()
        actual_df, actual_string = dv.processDatatype(final_df, format, results)

        pd.testing.assert_frame_equal(actual_df, expected_df)
        assert actual_string == expected_string

# Test processDataType csv type with sample result data
def test_processDatatype_csv_with_valid_results():
        final_df = pd.DataFrame()
        format = "csv"
        results = [
            {"type": "linecontributions", "filename": "file1", "data": pd.DataFrame({
                "commithash": ["12345", "67890"],
                "author": ["Alice", "Bob"],
                "date": ["2022-01-01", "2022-01-02"],
                "linenum": [1, 2],
                "content": ["line 1", "line 2"]
            })},
            {"type": "linecontributions", "filename": "file2", "data": pd.DataFrame({
                "commithash": ["54321", "09876"],
                "author": ["Alice", "Charlie"],
                "date": ["2022-01-03", "2022-01-04"],
                "linenum": [1, 2],
                "content": ["line 1", "line 2"]
            })}
        ]
        expected_df = pd.DataFrame({
            "author": ["Alice", "Bob", "Charlie"],
            "file1": [1.0, 1.0, 0.0],
            "file2": [1.0, 0.0, 1.0]
        })
        expected_string = ""

        dv = DataVisualization()
        actual_df, actual_string = dv.processDatatype(final_df, format, results)

        pd.testing.assert_frame_equal(actual_df.fillna(0), expected_df)
        # assert actual_df.fillna(0).to_string() == expected_df.to_string()
        assert actual_string == expected_string

# Test processDataType pdf type with sample result data
def test_processDatatype_pdf_with_valid_results():
        final_df = pd.DataFrame()
        format = "pdf"
        results = [
            {"type": "linecontributions", "filename": "file1", "data": pd.DataFrame({
                "commithash": ["12345", "67890"],
                "author": ["Alice", "Bob"],
                "date": ["2022-01-01", "2022-01-02"],
                "linenum": [1, 2],
                "content": ["line 1", "line 2"]
            })},
            {"type": "linecontributions", "filename": "file2", "data": pd.DataFrame({
                "commithash": ["54321", "09876"],
                "author": ["Alice", "Charlie"],
                "date": ["2022-01-03", "2022-01-04"],
                "linenum": [1, 2],
                "content": ["line 1", "line 2"]
            })}
        ]
        expected_df = pd.DataFrame({
            "author": ["Alice", "Bob", "Charlie"],
            "file1": [1.0, 1.0, 0.0],
            "file2": [1.0, 0.0, 1.0]
        })
        expected_string = ""

        dv = DataVisualization()
        actual_df, actual_string = dv.processDatatype(final_df, format, results)
        
        pd.testing.assert_frame_equal(actual_df.fillna(0), expected_df)
        # assert actual_df.fillna(0).to_string == expected_df.to_string
        assert actual_string == expected_string

# Test formatConversion to txt type with sample data
def test_formatConversion_txt():
    df = pd.DataFrame({'author': ['Alice', 'Bob'], 'lines': [8, 24]})
    dv = DataVisualization()
    dv.formatConversion(df, 'Alice: 8 lines\nBob: 24 lines', 'txt')
    with open('output.txt', 'r') as f:
        assert f.read() == 'Alice: 8 lines\nBob: 24 lines'

# Test formatConversion to csv type with sample data
def test_formatConversion_csv():
    df = pd.DataFrame({'author': ['Alice', 'Bob'], 'lines': [8, 24]})
    dv = DataVisualization()
    dv.formatConversion(df, '', 'csv')
    with open('output.csv', 'r') as f:
        assert f.read() == 'author,lines\nAlice,8\nBob,24\n'

# Test formatConversion to pdf type with sample data
def test_pdf_format():
    # create DataVisualization object and generate PDF
    df = pd.DataFrame({'author': ['Alice', 'Bob'], 'lines': [8, 24]})
    dv = DataVisualization()
    dv.formatConversion(df, "", "pdf")
    
    # extract text from PDF
    extractedText = extract_text("output.pdf")
    
    # define expected output
    expected_output = "lines\n\nBob\n\nAlice\n\n0\n\n5\n\n10\n\n15\n\n20\n\n25\n\nNumber of lines\n\n \n\x0c"
    
    # assert that the extracted text matches the expected output
    assert extractedText == expected_output