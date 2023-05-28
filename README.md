storm version - apache-storm-1.2.3
kafka version - kafka_2.13-2.8.1
hadoop version -hadoop 2-6-0

required python libraries
*pip install hdfs
*pip install streamparse
*git clone https://github.com/dpkp/kafka-python.git
cd kafka-python
pip install .

optional for confluent cloud
pip install confluent-kafka

others
sudo apt-get install leiningen
sudo apt install openjdk-8-jdk


#Hadoop
start-all.sh

#Kafa Commands
$KAFKA_DIR/bin/zookeeper-server-start.sh $KAFKA_DIR/config/zookeeper.properties
$KAFKA_DIR/bin/kafka-server-start.sh $KAFKA_DIR/config/server.properties

# Create a topic
$KAFKA_DIR/bin/kafka-topics.sh --create --topic test --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# List topics
$KAFKA_DIR/bin/kafka-topics.sh --list --bootstrap-server localhost:9092

# Describe a topic
$KAFKA_DIR/bin/kafka-topics.sh --describe --topic test --bootstrap-server localhost:9092

# Produce messages to a topic
$KAFKA_DIR/bin/kafka-console-producer.sh --topic test --bootstrap-server localhost:9092

# Consume messages from a topic
$KAFKA_DIR/bin/kafka-console-consumer.sh --topic test --bootstrap-server localhost:9092 --from-beginning


#Storm Commands
$STORM_HOME/bin/storm nimbus
$STORM_HOME/bin/storm supervisor


#Topology run command
 
The Topology run command should execute inside Kafka_storm directory
cd /path/Kafka-Storm && sparse run --name first_topology


PATH VARIABLES

export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin

export HADOOP_HOME=/home/ameen/apache/hadoop/hadoop-2.6.0-cdh5.4.1
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
export HADOOP_MAPRED_HOME="$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME"
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_INSTALL=$HADOOP_HOME

export KAFKA_DIR=/path/kafka_2.13-2.8.1
export PATH=$PATH:$KAFKA_DIR/bin
export PATH=$PATH:$KAFKA_DIR/config

export STORM_HOME=/hpath/apache-storm-1.2.3
export PATH=$PATH:$STORM_HOME/bin

export KAFKA_PYTHON=/path/Kafka-Storm

export LEIN_ROOT=true

etc ...





