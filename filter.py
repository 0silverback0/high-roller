class Filter:
    def __init__(self, bud, thc, brand, category):
        self.bud = bud
        self.thc = thc
        self.brand = brand
        self.category = category
        self.all_bud = bud.query.all()
        self.query = ''

    def query_filter(self):
        
        #get highest thc content, and brand names
        high = []
        brands = []
        for b in self.all_bud:
            high.append(b.thc)
            brands.append(b.brand)
        high_thc = max(high)
        
        if self.thc and self.brand:
            if int(self.thc) > int(high_thc) or self.brand not in brands:
                self.query = self.bud.query.all()
                return self.query
            else:
                self.query = self.bud.query.filter(self.bud.brand==self.brand).filter(self.bud.thc >= self.thc)

        elif self.thc and self.category:
            if int(self.thc) > int(high_thc):
                self.query = self.bud.query.all()
            else:
                self.query = self.bud.query.filter(self.bud.thc >= self.thc).filter(self.bud.category==self.category)

        elif self.brand and self.category:
            if self.brand in brands:
                self.query = self.bud.query.filter(self.bud.brand==self.brand, self.bud.category==self.category)
            else:
                self.query = self.bud.query.all()

        elif self.thc:
            if int(self.thc) > int(high_thc):
                self.query = self.bud.query.all()
            else:
                self.query = self.bud.query.filter(self.bud.thc >= self.thc)

        elif self.brand:
            if self.brand in brands:
                self.query = self.bud.query.filter(self.bud.brand==self.brand)
            else:
                self.query = self.bud.query.all()

        elif self.category:
            self.query = self.bud.query.filter(self.bud.category==self.category)
        else:
            self.query = self.bud.query.all()
        return self.query