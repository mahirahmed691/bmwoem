import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';
import { TextInput, Checkbox, List, Divider, ActivityIndicator } from 'react-native-paper';

const DataScreen = () => {
  const [bmwCombinations, setBmwCombinations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [filters, setFilters] = useState({
    Series: true,
    Body: true,
    Model: true,
    Market: true,
    Production_Month: true,
  });

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('/Users/mahirahmed/bmw-oem/data/bmw_combinations.json');

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const data = await response.json();
        setBmwCombinations(data || []);
      } catch (error) {
        console.error('Error reading data:', error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const filteredData = bmwCombinations.filter((combination) =>
    Object.keys(filters).some(
      (key) =>
        filters[key] &&
        combination[key] &&
        combination[key].toLowerCase().includes(searchQuery.toLowerCase())
    )
  );

  const renderItem = ({ item }) => (
    <List.Item
      title={`Series: ${item.Series}`}
      description={`Body: ${item.Body}\nModel: ${item.Model}\nMarket: ${item.Market}\nProduction Month: ${item.Production_Month}`}
      left={(props) => <Checkbox {...props} status={filters[item.Series] ? 'checked' : 'unchecked'} />}
    />
  );

  return (
    <View style={styles.container}>
      <TextInput
        mode="outlined"
        style={styles.searchInput}
        label="Search"
        value={searchQuery}
        onChangeText={(text) => setSearchQuery(text)}
      />
      <Divider style={styles.divider} />
      <List.Section>
        <List.Subheader>Filters</List.Subheader>
        <View style={styles.filtersContainer}>
          {Object.keys(filters).map((key) => (
            <View key={key} style={styles.filterOption}>
              <Checkbox
                status={filters[key] ? 'checked' : 'unchecked'}
                onPress={() =>
                  setFilters((prevFilters) => ({
                    ...prevFilters,
                    [key]: !prevFilters[key],
                  }))
                }
              />
              <Text style={styles.filterText}>{key}</Text>
            </View>
          ))}
        </View>
      </List.Section>
      <Divider style={styles.divider} />
      {loading ? (
        <ActivityIndicator style={styles.loader} size="large" color="#0000ff" />
      ) : (
        <FlatList
          data={filteredData.slice(0, 1000)}
          renderItem={renderItem}
          keyExtractor={(_, index) => index.toString()}
        />
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: '#fff',
  },
  searchInput: {
    marginBottom: 16,
  },
  divider: {
    marginVertical: 16,
  },
  loader: {
    marginTop: 16,
  },
  filtersContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
  },
  filterOption: {
    flexDirection: 'row',
    alignItems: 'center',
    marginRight: 16,
    marginBottom: 8,
  },
  filterText: {
    marginLeft: 8,
  },
});

export default DataScreen;
