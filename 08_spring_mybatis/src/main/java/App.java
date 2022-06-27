import Priv.wangjunqiang.domain.User;
import Priv.wangjunqiang.dao.UserDao;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.IOException;
import java.io.InputStream;

public class App {
    public static void main(String[] args) throws IOException {
        // 1. 加载配置文件
        String resource = "mybatis-config.xml";
        InputStream inputStream = Resources.getResourceAsStream(resource);

        // 2. 获取sqlSessionFactory
        SqlSessionFactory sqlSessionFactory =
            new SqlSessionFactoryBuilder().build(inputStream);

        // 3. 创建sqlSession
        SqlSession sqlSession = sqlSessionFactory.openSession();

        // 4.创建sql语句映射类
        UserDao mapper = sqlSession.getMapper(UserDao.class);

        // 5.获取数据
        User user = mapper.findById(1);

        System.out.println(user);

    }
}
