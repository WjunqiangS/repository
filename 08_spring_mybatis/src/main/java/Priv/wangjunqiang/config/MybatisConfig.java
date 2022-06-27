package Priv.wangjunqiang.config;

import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.mapper.MapperScannerConfigurer;
import org.springframework.context.annotation.Bean;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;

import javax.sql.DataSource;
import java.io.IOException;

public class MybatisConfig {

    @Bean
    public SqlSessionFactoryBean sqlSessionFactoryBean(DataSource dataSource)
        throws IOException {
        SqlSessionFactoryBean sqlSessionFactoryBean =
            new SqlSessionFactoryBean();

        // 给包设置别名替换<typeAliases>标签
        sqlSessionFactoryBean.setTypeAliasesPackage("Priv.wangjunqiang.domain");

        // 设置数据源替换Mybatis数据库设置
        sqlSessionFactoryBean.setDataSource(dataSource);

        // 设置sql映射文件位置
        sqlSessionFactoryBean.setMapperLocations(new PathMatchingResourcePatternResolver().getResources("classpath:Priv/wangjunqiang/dao/*.xml"));

        return sqlSessionFactoryBean;
    }

    @Bean
    public MapperScannerConfigurer mapperScannerConfigurer() {

        // 创建Mapper配置对象
        MapperScannerConfigurer mapperScannerConfigurer =
            new MapperScannerConfigurer();

        // 设置包所在位置替换<mappers>中的<package>包
        mapperScannerConfigurer.setBasePackage("Priv.wangjunqiang.dao");


        return mapperScannerConfigurer;
    }
}
