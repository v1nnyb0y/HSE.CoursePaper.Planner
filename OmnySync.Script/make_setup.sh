SETUP_NAME=full_setup.sh

if [ -n "$1" ]; then
    SETUP_NAME="$1"
fi

echo "[INFO] Writing to file $SETUP_NAME"

cat >$SETUP_NAME << EOL
#!/bin/bash
INSTALL_PATH=/opt/sync_notion
OMNIPLAN_SRC=/Users/*/Library/Application Scripts/com.omnigroup.OmniPlan3/
CP=/bin/cp

if [[ \$EUID -ne 0 ]]; then
    echo "[ERR ] This installer must be run as root!"
    exit
fi

pip3 install git+https://github.com/c0j0s/notion-py@master#egg=notion
if [ \$? -ne 0 ]; then
    echo "[ERR ] Notion not installed!"
    exit
fi

mkdir -p "\$INSTALL_PATH/data/tmp"
if [ \$? -ne 0 ]; then
    echo "[ERR ] Directories can't created!"
    exit
fi

touch "\$INSTALL_PATH/data/__init__.py"
if [ \$? -ne 0 ]; then
    echo "[ERR ]Files can't be created!"
    exit
fi
touch "\$INSTALL_PATH/data/tmp/__init__.py"
EOL

function write_file {
    path="\$INSTALL_PATH/$1"
    if [ -n "$2" ]; then
        path="$2/$1"
    fi
    echo >> $SETUP_NAME
    echo >> $SETUP_NAME
    echo "##### Writing file: ./$1 #####" >> $SETUP_NAME
    echo "cat >\"$path\" <<EOL" >> $SETUP_NAME
    cat $1 | sed -e 's/\$/\\\$/g' >> $SETUP_NAME
    echo >> $SETUP_NAME
    echo "EOL" >> $SETUP_NAME
    echo "echo \"[ OK ] File $1 writed!\"" >> $SETUP_NAME
    echo "##### End writing file ./$1 #####" >> $SETUP_NAME
    echo "[ OK ] File $1 writed!"
}

write_file data/task.py
write_file data/variables.py
write_file add_to_notion.py
write_file add_to_omny.py
write_file from_omny.sh
write_file to_omny.sh

cat >>$SETUP_NAME << EOL
chmod -R 777 \$INSTALL_PATH
chmod u+x "\$INSTALL_PATH/from_omny.sh"
chmod u+x "\$INSTALL_PATH/to_omny.sh"

cp -r *.scpt \$OMNIPLAN_SRC/
EOL