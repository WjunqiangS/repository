package Priv.wangjunqiang.config;

import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.mapper.MapperScannerConfigurer;
import org.springframework.context.annotation.Bean;
import org.springframework.core.io.Resource;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;

import javax.sql.DataSource;
import java.io.IOException;

public class MybatisConfig {
    @Bean
    public SqlSessionFactoryBean sqlSessionFactoryBean(DataSource dataSource)
        throws IOException {
        SqlSessionFactoryBean sqlSessionFactoryBean =
            new SqlSessionFactoryBean();
        sqlSessionFactoryBean.setTypeAliasesPackage("Priv.wangjunqiang.domain");

        sqlSessionFactoryBean.setMapperLocations(new PathMatchingResourcePatternResolver().getResources("classpath:Priv/wangjunqiang/dao/*Mapper.xml"));

        sqlSessionFactoryBean.setDataSource(dataSource);

        return sqlSessionFactoryBean;
    }

    @Bean
    public MapperScannerConfigurer mapperScannerConfigurer() {
        MapperScannerConfigurer mapperScannerConfigurer =
            new MapperScannerConfigurer();

        mapperScannerConfigurer.setBasePackage("Priv.wangjunqiang.dao");

        return mapperScannerConfigurer;
    }
}
