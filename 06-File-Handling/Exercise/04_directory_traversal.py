import os


def extract_files(dir):
    return [el for el in dir if os.path.isfile(el)]


def get_report_for_extensions(files):
    report = {}
    for file in files:
        file_name, extension = os.path.splitext(file)
        if extension not in report:
            report[extension] = []
        report[extension].append(file_name)
    return report


dir_content = os.listdir()

files = extract_files(dir_content)
report_info = get_report_for_extensions(files)

result_str = ""
for extension, file_names in sorted(report_info.items(), key=lambda x: x[0]):
    result_str += f"{extension}\n"
    for name in file_names:
        result_str += f"- - - {name}.{extension}\n"

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')     # -----> desktop path is always valid, regardless of the user.
final_location = desktop + os.path.sep + 'my_report_result.txt'

with open(final_location, "w") as file:
    file.write(result_str)











