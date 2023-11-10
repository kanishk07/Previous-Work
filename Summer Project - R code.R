library(plotly) 
library(umap) 
library(tidyverse)
library(readr)

cancer <- read_excel("D:/Documents/UTEP/Internship/Texas Tech/Hep3B GD AlDH+ and ALDH- 01 13 23 (2).xlsx")

cancer.data = cancer[, grep("Control ALDH+|GD ALDH+|Gene Expression", colnames(cancer))] 
cancer.labels = cancer[, "Type"] 
cancer.umap = umap(cancer.data, n_components = 3, random_state = 15) 
layout <- cancer.umap[["layout"]] 
layout <- data.frame(layout) 
final <- cbind(layout, cancer$Type) 

fig <- plot_ly(final, x = ~cancer$`Gene Expression`, y = ~cancer$`Gene Symbol`, color = ~cancer$Type, colors = c('#636EFA','#EF553B','#00CC96'), type = 'scatter', mode = 'markers')%>%  
  layout(
    plot_bgcolor = "white",
    legend=list(title=list(text='Type')), 
    xaxis = list( 
      title = "Gene Expression"),  
    yaxis = list( 
      title = "Genes")) %>%
  add_trace(marker = list(size = 15))

cancer.umap = umap(cancer.data, n_components = 3, random_state = 15) 
layout <- cancer.umap[["layout"]] 
layout <- data.frame(layout) 
final <- cbind(layout, cancer$Type) 

#fig2 <- plot_ly(final, x = ~X1, y = ~X2, z = ~X3, color = ~cancer$Type, colors = c('#636EFA','#EF553B','#00CC96')) 
#fig2 <- fig2 %>% add_markers() 
#fig2 <- fig2 %>% layout(scene = list(xaxis = list(title = '0'), 
#                                     yaxis = list(title = '1'), 
#                                     zaxis = list(title = '2'))) 

fig
#fig2

########################################

cancer.data = cancer[, grep("Control ALDH+|GD ALDH+|Gene Expression", colnames(cancer))] 
cancer.labels = cancer[, "Type"] 
cancer.umap = umap(cancer.data, n_components = 3, random_state = 15) 
layout <- cancer.umap[["layout"]] 
layout <- data.frame(layout) 
final <- cbind(layout, cancer$Type) 

fig <- plot_ly(final, x = ~cancer$`Gene Expression`, y = ~cancer$`Gene Symbol`, color = ~cancer$Type, colors = c('#636EFA','#EF553B','#00CC96'), type = 'scatter', mode = 'markers')%>%  
  layout(
    plot_bgcolor = "white",
    legend=list(title=list(text='Type')), 
    xaxis = list( 
      title = "Genes"),  
    yaxis = list( 
      title = "Gene Expression")) 

cancer.umap = umap(cancer.data, n_components = 3, random_state = 15) 
layout <- cancer.umap[["layout"]] 
layout <- data.frame(layout) 
final <- cbind(layout, cancer$Type) 

fig2 <- plot_ly(final, x = ~X1, y = ~X2, z = ~X3, color = ~cancer$Type, colors = c('#636EFA','#EF553B','#00CC96')) 
fig2 <- fig2 %>% add_markers() 
fig2 <- fig2 %>% layout(scene = list(xaxis = list(title = '0'), 
                                     yaxis = list(title = '1'), 
                                     zaxis = list(title = '2'))) 

#fig

fig2
#########################################################

cancer.data = cancer[, grep("Control ALDH+|GD ALDH+|Gene Expression", colnames(cancer))] 
cancer.labels = cancer[, "Regulation"] 
cancer.umap = umap(cancer.data, n_components = 3, random_state = 15) 
layout <- cancer.umap[["layout"]] 
layout <- data.frame(layout) 
final <- cbind(layout, cancer$Regulation) 

fig <- plot_ly(final, x = ~cancer$`Gene Expression`, y = ~cancer$`Gene Symbol`, color = ~cancer$Regulation, colors = c('#636EFA','#EF553B','#00CC96'), type = 'scatter', mode = 'markers')%>%  
  layout(
    plot_bgcolor = "white",
    legend=list(title=list(text='Regulation')), 
    xaxis = list( 
      title = "Gene Expression"),  
    yaxis = list( 
      title = "Genes")) %>%
  add_trace(marker = list(size = 15))

cancer.umap = umap(cancer.data, n_components = 3, random_state = 15) 
layout <- cancer.umap[["layout"]] 
layout <- data.frame(layout) 
final <- cbind(layout, cancer$Regulation) 

#fig2 <- plot_ly(final, x = ~X1, y = ~X2, z = ~X3, color = ~cancer$Regulation, colors = c('#636EFA','#EF553B','#00CC96')) 
#fig2 <- fig2 %>% add_markers() 
#fig2 <- fig2 %>% layout(scene = list(xaxis = list(title = '0'), 
#                                     yaxis = list(title = '1'), 
#                                     zaxis = list(title = '2'))) 

fig

#fig2
######################################################################################

cancer.data = cancer[, grep("Control ALDH+|GD ALDH+|Gene Expression", colnames(cancer))] 
cancer.labels = cancer[, "Gene Symbol"] 
cancer.umap = umap(cancer.data, n_components = 3, random_state = 15) 
layout <- cancer.umap[["layout"]] 
layout <- data.frame(layout) 
final <- cbind(layout, cancer$`Gene Symbol`) 

fig <- plot_ly(final, x = ~cancer$Type, y = ~cancer$`Gene Expression`, color = ~cancer$`Gene Symbol`, colors = c('#636EFA','#EF553B','#00CC96'), type = 'scatter', mode = 'markers')%>%  
  layout(
    plot_bgcolor = "white",
    legend=list(title=list(text='Gene Symbol')), 
    xaxis = list( 
      title = "Type"),  
    yaxis = list( 
      title = "Genes Expression")) 

cancer.umap = umap(cancer.data, n_components = 3, random_state = 15) 
layout <- cancer.umap[["layout"]] 
layout <- data.frame(layout) 
final <- cbind(layout, cancer$`Gene Symbol`) 

#fig2 <- plot_ly(final, x = ~X1, y = ~X2, z = ~X3, color = ~cancer$Type, colors = c('#636EFA','#EF553B','#00CC96')) 
#fig2 <- fig2 %>% add_markers() 
#fig2 <- fig2 %>% layout(scene = list(xaxis = list(title = '0'), 
#                                     yaxis = list(title = '1'), 
#                                     zaxis = list(title = '2'))) 

fig
###################################################################

cancer.data = cancer[, grep("Control ALDH+|GD ALDH+|Gene Expression", colnames(cancer))] 
cancer.labels = cancer[, "Type"] 
cancer.umap = umap(cancer.data, n_components = 3, random_state = 15) 
layout <- cancer.umap[["layout"]] 
layout <- data.frame(layout) 
final <- cbind(layout, cancer$Type) 

fig <- plot_ly(final, x = ~cancer$`Control ALDH+`, y = ~cancer$`GD ALDH+`, color = ~cancer$Type, colors = c('#636EFA','#EF553B','#00CC96'), type = 'scatter', mode = 'markers')%>%  
  layout(
    plot_bgcolor = "white",
    legend=list(title=list(text='Gene Symbol')), 
    xaxis = list( 
      title = "Control ALDH+"),  
    yaxis = list( 
      title = "GD ALDH+")) %>%
  add_markers(marker = list(size = 20)) 

cancer.umap = umap(cancer.data, n_components = 3, random_state = 15) 
layout <- cancer.umap[["layout"]] 
layout <- data.frame(layout) 
final <- cbind(layout, cancer$Type) 

#fig2 <- plot_ly(final, x = ~X1, y = ~X2, z = ~X3, color = ~cancer$Type, colors = c('#636EFA','#EF553B','#00CC96')) 
#fig2 <- fig2 %>% add_markers() 
#fig2 <- fig2 %>% layout(scene = list(xaxis = list(title = '0'), 
#                                     yaxis = list(title = '1'), 
#                                     zaxis = list(title = '2'))) 

fig

###########################################################################

cancer.data = cancer[, grep("Control ALDH+|GD ALDH+|Gene Expression", colnames(cancer))] 
cancer.labels = cancer[, "Type"] 
cancer.umap = umap(cancer.data, n_components = 3, random_state = 15) 
layout <- cancer.umap[["layout"]] 
layout <- data.frame(layout) 
final <- cbind(layout, cancer$Type) 

fig <- plot_ly(final, x = ~X1, y = ~X2, color = ~cancer$Type, colors = c('#636EFA','#EF553B','#00CC96'), type = 'scatter', mode = 'markers')%>%  
  layout(
    plot_bgcolor = "white",
    legend=list(title=list(text='Type')), 
    xaxis = list( 
      title = "X1"),  
    yaxis = list( 
      title = "X2")) %>%
  add_markers(marker = list(size = 20))

cancer.umap = umap(cancer.data, n_components = 3, random_state = 15) 
layout <- cancer.umap[["layout"]] 
layout <- data.frame(layout) 
final <- cbind(layout, cancer$Type) 

#fig2 <- plot_ly(final, x = ~X1, y = ~X2, z = ~X3, color = ~cancer$Type, colors = c('#636EFA','#EF553B','#00CC96')) 
#fig2 <- fig2 %>% add_markers() 
#fig2 <- fig2 %>% layout(scene = list(xaxis = list(title = '0'), 
#                                     yaxis = list(title = '1'), 
#                                     zaxis = list(title = '2'))) 

fig

##################################################################################

cancer.data = cancer[, grep("Control ALDH+|GD ALDH+|Gene Expression", colnames(cancer))] 
cancer.labels = cancer[, "Regulation"] 
cancer.umap = umap(cancer.data, n_components = 3, random_state = 15) 
layout <- cancer.umap[["layout"]] 
layout <- data.frame(layout) 
final <- cbind(layout, cancer$Regulation) 

fig <- plot_ly(final, x = ~X1, y = ~X2, color = ~cancer$Regulation, colors = c('#636EFA','#EF553B','#00CC96'), type = 'isosurface', mode = 'markers')%>%  
  layout(
    plot_bgcolor = "white",
    legend=list(title=list(text='Regulation')), 
    xaxis = list( 
      title = "X1"),  
    yaxis = list( 
      title = "X2")) %>%
  add_markers(marker = list(size = 20)) 

cancer.umap = umap(cancer.data, n_components = 3, random_state = 15) 
layout <- cancer.umap[["layout"]] 
layout <- data.frame(layout) 
final <- cbind(layout, cancer$Regulation) 

#fig2 <- plot_ly(final, x = ~X1, y = ~X2, z = ~X3, color = ~cancer$Type, colors = c('#636EFA','#EF553B','#00CC96')) 
#fig2 <- fig2 %>% add_markers() 
#fig2 <- fig2 %>% layout(scene = list(xaxis = list(title = '0'), 
#                                     yaxis = list(title = '1'), 
#                                     zaxis = list(title = '2'))) 

fig

#########################################################################

cancer.data = cancer[, grep("Control ALDH+|GD ALDH+|Gene Expression", colnames(cancer))] 
cancer.labels = cancer[, "Type"] 
cancer.umap = umap(cancer.data, n_components = 3, random_state = 15) 
layout <- cancer.umap[["layout"]] 
layout <- data.frame(layout) 
final <- cbind(layout, cancer$Type) 

fig <- plot_ly(final, x = ~cancer$`Gene Expression`, y = ~cancer$`Gene Symbol`, color = ~cancer$Type, colors = c('#636EFA','#EF553B','#00CC96'), type = 'scatter', mode = 'markers')%>%  
  layout(
    plot_bgcolor = "white",
    legend=list(title=list(text='Type')), 
    xaxis = list( 
      title = "Genes"),  
    yaxis = list( 
      title = "Gene Expression")) 

cancer.umap = umap(cancer.data, n_components = 3, random_state = 15) 
layout <- cancer.umap[["layout"]] 
layout <- data.frame(layout) 
final <- cbind(layout, cancer$Type) 

fig2 <- plot_ly(final, x = ~cancer$`Gene Expression`, y = ~cancer$`Control ALDH+`, z = ~cancer$`GD ALDH+`, color = ~cancer$Type, colors = c('#636EFA','#EF553B','#00CC96'))
fig2 <- fig2 %>% add_markers() 
fig2 <- fig2 %>% layout(scene = list(xaxis = list(title = 'Gene Expression'), 
                                     yaxis = list(title = 'Control ALDH+'), 
                                     zaxis = list(title = 'GD ALDH+'))) 

#fig

fig2
