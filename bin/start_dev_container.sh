image="parflow/python_dev_environment:latest";
container_name="parflow_dev";
mount_location="${PWD}/";
while getopts i:c:m: flag
do
    case "${flag}" in
        i) image=${OPTARG};;
        c) container_name=${OPTARG};;
        m) mount_location=${OPTARG};;
    esac
done
docker run --rm -it --env=DISPLAY --name=${container_name} -e LANG=en_US.utf8 -v ${mount_location}:/data/  ${image}