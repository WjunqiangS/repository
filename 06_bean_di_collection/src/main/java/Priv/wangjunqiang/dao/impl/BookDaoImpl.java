package Priv.wangjunqiang.dao.impl;

import Priv.wangjunqiang.dao.BookDao;

import java.util.*;

public class BookDaoImpl implements BookDao {

    private int[] array;

    private List<String> list;

    private Set<String> set;

    private Map<String, String> map;

    private Properties properties;

    @Override
    public void save() {
        System.out.println("book dao save....");
        System.out.println("array:" + Arrays.toString(array));
        System.out.println("list:" + list);
        System.out.println("set:" + set);
        System.out.println("map:" + map);
        System.out.println("properties:" + properties);
    }

    public int[] getArray() {
        return array;
    }

    public void setArray(int[] array) {
        this.array = array;
    }

    public List<String> getList() {
        return list;
    }

    public void setList(List<String> list) {
        this.list = list;
    }

    public Set<String> getSet() {
        return set;
    }

    public void setSet(Set<String> set) {
        this.set = set;
    }

    public Map<String, String> getMap() {
        return map;
    }

    public void setMap(Map<String, String> map) {
        this.map = map;
    }

    public Properties getProperties() {
        return properties;
    }

    public void setProperties(Properties properties) {
        this.properties = properties;
    }
}
