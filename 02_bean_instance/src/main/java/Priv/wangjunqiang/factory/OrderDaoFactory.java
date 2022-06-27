package Priv.wangjunqiang.factory;

import Priv.wangjunqiang.dao.OrderDao;
import Priv.wangjunqiang.dao.impl.OrderDaoImpl;

public class OrderDaoFactory {
    OrderDaoFactory () {
        System.out.println("OrderDao Factory...");
    }
    public static OrderDao getOrderDao() {
        System.out.println("order dao setup...");
        return new OrderDaoImpl();
    }
}
