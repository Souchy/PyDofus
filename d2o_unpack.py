import io, sys, os, json
from pydofus.d2o import D2OReader, InvalidD2OFile

# python d2o_unpack.py (all files in input folder)
# folder output: ./output/{all files}

path_input = "input/"
path_output = "output/"

for subdir, dirs, files in os.walk(path_input):
    for file in os.listdir(subdir):
        if file.endswith(".d2o"):
            file_name = os.path.basename(file)
            d2p_file = open(subdir + "/" + file, "rb")
            out_dir = (subdir + "/").replace(path_input, path_output)

            # print("D2O Unpacker for " + file_name)

            try:
                d2o_reader = D2OReader(d2p_file)
                d2o_data = d2o_reader.get_objects()

                json_output = open(out_dir + file_name.replace("d2o", "json"),
                                "w")
                json.dump(d2o_data, json_output, indent=4)
                json_output.close()
            except InvalidD2OFile:
                pass
