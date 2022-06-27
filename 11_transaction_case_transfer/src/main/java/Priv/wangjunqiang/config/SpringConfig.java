package Priv.wangjunqiang.config;

import org.apache.ibatis.transaction.Transaction;
import org.springframework.context.annotation.*;
import org.springframework.jdbc.datasource.DataSourceTransactionManager;
import org.springframework.transaction.annotation.EnableTransactionManagement;

import javax.sql.DataSource;

@Configuration
@PropertySource("classpath:jdbc.properties")
@ComponentScan("Priv.wangjunqiang")
@Import({JdbcConfig.class, MybatisConfig.class})
// 开启事务
@EnableTransactionManagement
public class SpringConfig {
    // 创建管理DataSource的事务管理Bean
    @Bean
    public DataSourceTransactionManager dataSourceTransactionManager(DataSource dataSource) {
        DataSourceTransactionManager dataSourceTransactionManager =
            new DataSourceTransactionManager();

        dataSourceTransactionManager.setDataSource(dataSource);

        return  dataSourceTransactionManager;
    }
}
